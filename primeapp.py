#!/usr/bin/env python
# coding: utf-8
#Reda Mastouri ©2021
#https://redamastouri.com/
#https://github.com/RedaMastouri/
#https://www.linkedin.com/in/reda-mastouri/
#https://www.freecodecamp.org/redamastouri

#App builder
import streamlit as st 
from PIL import Image 



# ========================================  Needed Functions SPACE: ==================================================:


def prime_tester(num):

    # prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               st.info(str(num)+" is not a prime number")
               st.success(str(i)+" times "+str(num//i)+" is "+str(num))
               return False
               break
       else:
            st.warning(str(num)+" is a prime number")
            return True

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        st.warning(str(num)+" is not a prime number")
        return False 


def prime_finder(num):
    is_prime = [True]*num
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(num**0.5+1), 2):
        index = i*2
        while index < num:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, num, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


def prime_number_sum_splitter(treshold):
    '''
    Prompting to user to type in a treshold 
    '''
    #Variables:
    count = 0
    primeUtils = [] #to store all prime numbers within the treshold
   
    
    #=========
    #treshold = int(input("Please type in a treshold value where you would like to find the highest prime number: "))

               
    #FASTEST COMPUTATION
    primeUtils = prime_finder(treshold)
            
            
    lastindex = len(primeUtils)
    maxValue = 0
    listOfOutcomes = [] #to store the exact ement to make up the sum
    
    #Finding the maxValue, and elements to make up the largest prime within the treshold
    for i in range(len(primeUtils)+1):
        for j in range(i+count, lastindex):
            elements = sum(primeUtils[i:j])
            if elements < treshold:
                if elements in primeUtils:
                    count = j-i
                    maxValue = elements
                    listOfOutcomes.append(primeUtils[i:j])
            else:
                lastindex = j+1
                break
    
    #Formatted output
    culumative= (" {total} = ".format(total = maxValue))
    formatted_formula = str(listOfOutcomes[-1])[1:-1].replace(",", " +")
    
    st.success("The prime {maximum} can be written as the sum of "          
              "{count} consecutive primes as follows: \n\n\n"          
              " {split}".format(maximum =maxValue, 
                            count=count,
                            split=culumative+formatted_formula))
    return 200




# ========================================  INTORODUCTORY SPACE: ==================================================:
with open("images/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
st.title("Prime Numbers- Project Euler")
st.subheader("By Reda Mastouri")

col1, col2, col3 = st.columns([1,3,1])
img=Image.open('images/prime.png')
col2.image(img,use_column_width=True)
st.info("Finding which prime, below a defined treshold, can be written as the sum of the most consecutive primes")



# Using the "with" syntax
with st.form(key='my_form'):
    text_input = st.text_input(label='Please type in a treshold value where you would like to find the highest prime number:')
    compute_button = st.form_submit_button(label='💻 Compute')

    if compute_button:
        st.write(prime_number_sum_splitter(int(text_input)))


# Check if the number found is a prime number
# Using the "with" syntax
with st.form(key='my_form2'):
    text_input = st.text_input(label='Verifying if the sum is a prime number:')
    compute_button = st.form_submit_button(label='✔️ Check')

    if compute_button:
        st.write(prime_tester(int(text_input)))

#footer
"Made in 🇺🇸 with ❤️ by Reda Mastouri ©2021"
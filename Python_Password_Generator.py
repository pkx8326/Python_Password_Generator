#!/usr/bin/env python
# coding: utf-8

# In[93]:


#Password generator
import random
#constants

#Character list (generated from ASCII code)
alpha = []
for i in range(97,123):
    alpha.append(chr(i))
    
for i in range(65,91):
    alpha.append(chr(i))

#number list    
num = ['0','1','2','3','4','5','6','7','8','9']

#symbol list
sym = ['~','`','!','#','$','%','^','&','*','(',')','-','_','+','=','[',']','|','\\',':',';','"','\'']

#Begin the program
print("Welcome to the Password Generator!")

#Keep asking input from user until the correct value (number) is obtained
while True: 
    try:
        nr_letters = int(input("How many letters do you want? "))
        break
    except ValueError:
        print("Try again...")
        
#Keep asking input from user until the correct value (number) is obtained        
while True:
    try:
        nr_numbers = int(input("How many numbers do you want? "))
        break
    except ValueError:
        print("Try again...")

#Keep asking input from user until the correct value (number) is obtained
while True:
    try:
        nr_symbols = int(input("How many symbols do you want? "))
        break
    except ValueError:
        print("Try again...")
        

#Create an empty list to contain the generated password
password_list = []

#collect randomized letters
x = 0
while x < nr_letters:
    password_list.append(alpha[random.randint(0,len(alpha))])
    x+=1


#collect randomized numbers
x = 0
while x < nr_numbers:
    password_list.append(num[random.randint(0,len(num))])
    x+=1
    

#collect randomized symbols
x = 0
while x < nr_symbols:
    password_list.append(sym[random.randint(0,len(sym))])
    x+=1


#Shuffle the items in the password_list list
password_list = random.sample(password_list, len(password_list))

#Create an empty password string
password = ""

# Concatenate all the randomized and shuffled items to create a password according to the numbers of letters, numbers, 
# and symbols specified by the user

for i in range(0,len(password_list)):
    password = password + password_list[i]

print(password)


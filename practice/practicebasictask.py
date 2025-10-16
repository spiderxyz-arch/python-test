# ----------------------------------------
# Assignment: Basic Python Data Types & Input
# Author: [Muhammad]
# Description:
# This program takes user's name, age, and hobby as input,
# then prints a personalized introduction message.
# It also shows some basic string functions.
# ----------------------------------------
#taking input from user:
name = input('enter your name :') # name input  
age = input("enter your age:")    # age  input
hobby=str(input("enter your favourite hobby :")) # hobby input 
print("hello my name is "+name+" i am " +age+" years old and my faviourate hobby is "+hobby+"ッ")
print(hobby.lower())     #convert the str into lower letter.
print(hobby.upper()) #convert the str into capital letter.
print(hobby.__len__())    #tell the number character of the str.

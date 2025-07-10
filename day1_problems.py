#1. Printing hello world

print("Hello,Python World!")

#2. Ask the user for their name and age, then print a greeting message.

name=input("Enter You name : ")
age=int(input("Enter your age: "))

print(f"Hi {name},your age is {age} years old !")

#3. 3. Demonstrate indentation in Python using an if statement.

age_of_boy=17
if age_of_boy>=18:
    print("You are eligible to caste your vote")
else:
    print("Sorry you are not eligible")

#4. 4. Create a file sum_numbers.py that asks for two numbers and prints their sum.

num1=int(input("Enter the value of num1: "))
num2=int(input("Enter the value of num2 : "))

print(f"Printing the sum of two numbers : {num1} + {num2} = {num1+num2}")

# 5. Display the bytecode of a function using the dis module.

import dis

def greet_me():
    print(f"Hello good morning")

dis.dis(greet_me)

# 6. Use pip to install a package and import it.

import math
print(math.pi)

# 7. In Jupyter Notebook, write a cell to calculate the square of a number.

def square(number):
    return number**2

number=4

print(f"the squre of a {number} is : {square(number)}")

# 8. Compare Python with C using comments in a .py file.

#Sum of two numbers in python & c
a=10
b=12
print(a+b)

#Addition code

'''
int num1=12
int num2=12
int sum=num1+num2
printf("%d,sum)

'''
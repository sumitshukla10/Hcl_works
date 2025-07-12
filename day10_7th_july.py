# Day 10 problem assignments concluded - Sumit Shukla

# 1. Explain the difference between 'import module' and 'from module import function'.

'''  
Import Module -> It imports the entire module and we have to use the module name to use it in our python script
eg. import math , import sys , import os 

From module import function -> it imports the specific functionalities of any particular module 
eg. from math import sqrt
'''

# 2. Write a Python program that imports the math module and prints the square root of 49.

import math
num=int(input("Enter the value of num : "))
print(f"The square root of given number {num} is : {math.sqrt(num)}")

# 3. What is a module and how is it different from a package?

print("Module - > A module is a single pyhton file containing functions classes ")

print("\n")

print("Package-> A package is a directory with an __int__.py file and can contain multiple module")

print("\n")

# 6. Write a program that prints the calendar of July 2025

import calendar
print(calendar.month(2025,12))

# 7. How does Python ensure randomness? Name two functions from the random module.

print("Python uses the mersenne twister algirithm to generate pseudo random numbers")

'''
eg 
random.randint(1,10)
random.choice([2,23,4,5,6,67,10])

'''

# 8. Write a program to generate a random number between 1 and 100 and check if it is divisible by 5.

import random

number=random.randint(1,100)
print(f"Random numbers are : {number}")

if num%5==0:
    print("NUmber is Divisible by 5")
else:
    print("Number is not divisible by 5 ")

# 9. What is the use of datetime module?

print("The datetime module is uesd to work with date and times for craeting formatting and manipulating stiff based on dates and times")

# 10. Write a program that displays the current date and time in the format: YYYY-MM-DD HH:MM:SS.

from datetime import datetime

time=datetime.now()
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# 11. What are differences between CSV and Excel file handling in Python?

print("CSV- Its a file formate for storinmg larger data into a single file in a structured way")

print("\n")

print("Excel -> Its an another file formate for storing data into an excel file")

# 12. Write a program using pandas to read a CSV file and convert it into an Excel file.

import pandas as pd
df=pd.read_csv('sample_data.csv')
df.to_excel('data.xlsx',index=False)

# 13. List three useful functions provided by the os module.

print("Three usesful functions are as follows :")
print("os,getcwd() - to get current working directory")
print("os.listdir()- list files of a directory")
print("os.mkdir()-to create a new folder using this command")

# 14. Write a program to create a folder named 'TestFolder' and list all files in the current directory.

import os
os.mkdir("sample")
files=os.listdir('.')
print(files)

# 15. What is the purpose of the glob module in Python?

print("The glob module is used to find files and directories using wildcards like .txt etc")

# 16. Write a Python program to list all '.txt' files in the current directory

import glob
file=glob.glob("*.txt")
print(file)

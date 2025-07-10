# Day 2 of problem solving -SUMIT SHUKLA 

# Q1: Write a program that accepts the user's name and age and prints a message?

username=input("Enter your name : ")
age=int(input("Enter your age : "))

print(f"Your username is {username} and your age is {age}")

# Q2: Write a Python program to calculate the area of a circle given the radius by the user?


radius=int(input("Enter the radius : "))
area=3.14*radius*radius

print(f"The are of cirle with the given radius {radius} is {area}")

# Q3: Write a program that checks if a number is even or odd using input from the user?

num=int(input("Enter the value of num : "))

if num%2==0:
    print("Entered number is even")
else:
    print("Entered number is odd ")

# Q4: Write a Python program to evaluate the expression 5 + 3 * 2 and explain the output based on operator precedence?

exp=5+3*2

#The result will evaluate on the basis of operator precedence first multiplication will evaluate and then additon 3*2=6 , 6+5 =11

print("The result of given expression is : ",exp)

# Q5: Write a program that reads a value from the user and prints its data type?

name=input("Enter Your name : ")
age=int(input("Enter your age : "))

print(f"the data type of name is {type(name)} and data type of age is {type(age)}")

# Q6: Write a Python program to reverse a string input by the user ?

Name=input("Enter your full name : ")

print(f"Before reverse the full name is {Name}")

reverseName=name[::-1]

print("After reversing the string the name is : ",reverseName)
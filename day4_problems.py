#Day4 of solving the  assignment problems - Sumit Shukla

# Q1. Define a function to calculate the factorial of a number (using recursion).

def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)

print(f"Factorial  of given number is : {factorial(5)}")

# Q2. Write a function that accepts any number of numbers using *args and returns their average.

def average_of_numbers(*args):
    result=sum(args)
    return result/len(args)

print(f"The average value of the following numbers is : {average_of_numbers(92,64,78)}")

# Q3. Create a function that accepts name and age (using keyword arguments) and prints a message.

def personal_msg(name,age):
    print(f"Hello {name} your age is {age} years old")

personal_msg("sumit",22)
personal_msg(age=23,name="Amit")

# Q4. Write a function that takes a list and returns a list with squared values using map().

lst=[1,2,3,4,5,6,7,8,9]
newList=[]

def square(x):
    return x**2

def squared_list(lst):
    return list(map(square,lst))

print(squared_list([1,2,3,4,5]))

# Q5. Demonstrate the use of filter() to extract even numbers from a list.

def even_checker(num):
    return num%2==0

nums=[2,3,4,5,6,7,8,9]
evenNums=list(filter(even_checker,nums))
print(f"Even numbers in the list are : {evenNums}")

# Q6. Create a function that returns both the max and min of a list (returning multiple values).

def get_max_min_values(lst):
    print(f"Maximum number is : {max(lst)}")
    print(f"Minimum number is : {min(lst)}")

get_max_min_values([2,3,4,56,71,1,100])

# Q7. Show an example of local and global variable conflict, and use global keyword to resolve it.

n=2
def change():
    global x 
    x=10
change()

print("value of x:",x)

# Q8. Use zip() to combine two lists: one of names and one of scores.

names = ["Aditya", "Sumit", "Pratham"]
ages = [22, 21, 29]
combined_result= list(zip(names, ages))
print(f"The result using the ZIP is {combined_result}")

# Q9. Import the math module and use math.sqrt() inside a function.

import math

def square_of_number(num):
    print(f"Square root of given number {num} is {math.sqrt(num)}")

square_of_number(36)
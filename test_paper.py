# What is the output of the following code and why
x=[1,2,3]
y=x
y+=[4,5]
print(x)

# the output of the following above code is to be [1, 2, 3, 4, 5] as we are shallow copying the values of x into y and then adding the values 4,5 which unlimately results into 1,2,3,4,5

# Differentiate between `is`, `==`, and `is not` operators with code examples.

# The `is` operator checks if two variables point to the same object in memory.
# The `==` operator checks if the values of two variables are equal.
# The `is not` operator checks if two variables do not point to the same object in memory.

# Predict the output: def func(a=[]): a.append(1) return a print(func()) print(func())
# The output of the above code will be:
# [1]

def func(a=[]):
    a.append(1)
    return a
print(func())   # the ouput will be [1] as we are appending 1 to the list a which is initialized as an empty list
print(func()) # the output will be [1, 1] as the list a is mutable and retains its state between function calls, so it appends another 1 to the existing list.

# How does Python manage variable scope and shadowing inside functions?

print(f"Variable scope in Python is managed using the LEGB rule: Local, Enclosing, Global, Built-in.")

print("\n")

print(f"Variables defined inside a function are local to that function. If a variable is not found in the local scope, Python looks for it in the enclosing scope, then in the global scope, and finally in the built-in scope.")

# Write a Python program to determine whether a string is a valid identifier.

import re
def is_valid_identifier(s):
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', s))
test_strings = ["sumit_shukla", "10Amit", "_ishappy", "birthday-one-10july", "user12345", "monsoon raining ??"]
for s in test_strings:
    if is_valid_identifier(s):
        print(f"{s} is a valid identifier.")
    else:
        print(f"{s} is not a valid identifier.")

# Explain operator precedence with an example where results change based on parentheses.

print("\nOperator precedence in Python determines the order in which operations are evaluated. For example, in the expression 2+2*5, multiplication has higher precedence than addition, so it is evaluated first.")
print("The precedence is as follows first divide, then multiply, then add, and finally subtract")

# What is the result of using `not a or b and c` when `a = False`, `b = True`, `c = False`?

a = False
b = True    
c = False
result = not a or b and c
print(a)
print(b)
print(c)
print(f"the  result is {result}")

# Write code to mimic a switch-case using match-case or dictionary-based approach.
num1=int(input("Enter the value of num1 : "))
num2=int(input("Enter th value of num2 : "))

operation=input("Operations available are : + - * / // ")
match operation:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        print(num1/num2)
    case '//':
        print(num1//num2)
    case _:
        print("Kindly choose a valid operation")

# Write a pattern printing program using nested loops for this pattern:
#*
#**
#***
#****
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

# Explain how the `assert` statement works. How is it different from `raise`?
print("\nThe `assert` statement is used for debugging purposes. It tests a condition and raises an AssertionError if the condition is false. It is typically used to catch bugs during development.")
print("The `raise` statement is used to explicitly raise an exception, which can be caught and handled by the program. It is used to signal that an error has occurred.")

# Explain pass-by-object-reference with this example
def modify_list(lst):
    lst.append(100)
l=[10,20]
modify_list(l)
print(l)

print(f"In pass by refernce the refeerence of the original memmory is passed and chnages can be seen if any made to the original object")
    

# Write a function that returns the sum of even-indexed Fibonacci numbers up to N.
def fibonacci_sum_even_index(n):
    a, b = 0, 1
    total = 0
    index = 0
    while a <= n:
        if index % 2 == 0:
            total += a
        a, b = b, a + b
        index += 1
    return total
print(fibonacci_sum_even_index(10))

# What is the output? Explain.
print(f"As we know that fibonacci series is a series of numbers where each number is the sum of its previous two numbers")

# What is the output? Explai
def foo(a,b=[]):
    b.append(a)
    return b
print(foo(1))
print(foo(2))

print(f"the output of above code is [1] and [1,2] because we know that the list is mutable and retains its state between functions call so the second call will append the 2 in the existing list of [1]")

# How would you return multiple values from a function? Show three ways.
def return_multiple_values():
    return 10,12,12
def return_multiple_values_list():
    return [100,200,300]        
def return_multiple_values_dict():
    return {'a': "Sumit", 'b': "bibash", 'c': "Aditya"}

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num - 1)

print(F"tHE FACTORIAL  of  given number is {factorial(5)}")


# Use map and filter together to find square of all even numbers from a list.
def square_even_numbers(numbers):
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))


# numbers=[1,2,3,4,5,6,7,8,9,10]
num=int(input("enter the number of nums :"))
numbers=[]
for i in range(num):
    n=int(input("Enter the value of n : "))
    numbers.append(n)
print(numbers)
print(square_even_numbers(numbers) )

#What is the diff betwwen args and kwargs

print("Args are used to specify that a functions can accept any number of arguments while kwargs are used to pass keyword arguments to a function. Args are passed as a tuple while kwargs are passed as a dictionary.")

#args and kwargs 

def example_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
example_function(10,20,30, name="sumit shukla", age=22)

def addition_of_number(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(f"sum of given numbers are {addition_of_number(1,2,3,4,5,56)}")

# Write a lambda function to sort a list of tuples based on the second element.
def sorted_tuple_helper(tups):
    return sorted(tups, key=lambda x: x[1])

# Example usage
tups = [(1, 3), (2, 1), (4, 2)]

# Explain how Python handles default arguments. What's the danger with mutable types

print(f"When default arguments is passed it is early evaluated by python and if mutuable type is used as a default argumnent then it may result into an unexpeted behaviour as default arguments is shared across all the functions call and program")

# Write a list comprehension to flatten a 2D list
def flatten_2d_list(two_d_list):
    return [item for sublist in two_d_list for item in sublist]
# Example usage
two_d_list = [[1, 2, 3], [4, 5], [6, 7]]        
print(flatten_2d_list(two_d_list))

# Write a Python code to count the frequency of words in a sentence using a dictionary.


# Explain the role of `super()` with multiple inheritance. Provide code.

print(f"The super keword is used to use all the functiins and methods of the parent class into the subclasss or the child class.Suped is a reserved keyword and can be used in child class to access the methods ")

# What are inner classes? Show a use case where they make sense.
print(f"Inner classes are classes defined within another class. They are used to logically group classes that are only used in one place, which helps in keeping the code organized and encapsulated.")
class OuterClass:
    class InnerClass:
        def inner_method(self):
            return "This is an inner class method."
    
    def outer_method(self):
        inner_instance = self.InnerClass()
        return inner_instance.inner_method()    
    
outer_instance = OuterClass()
print(outer_instance.outer_method())


# Write an efficient algorithm to find the second largest element in a list without sorting
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None

numbers = [3, 1, 4, 4, 5, 2]
print(second_largest(numbers))  

# Write a Python code to count the frequency of words in a sentence using a dictionary.
def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        word = word.lower()  # Normalize to lowercase
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
sentence = "We are here at Bennett UNiversity and leanrning pyhton with our mentor Mr. Sumit kumar roy and Mr. Shivashish Sir"
print(word_frequency(sentence))

# Given two lists, return the elements common to both using list comprehension and sets.

def common_elements(l1, l2):
    return [element for element in set(l1) if element in set(l2)] 
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8] 
print(common_elements(l1, l2))

# What is the difference between `del`, `pop()`, and `remove()` in lists?

print(f"`del`, `pop()`, and `remove()` are all methods used to remove elements from a list, but they work differently:")

print(f"The `del` statement removes an item at a specific index or the entire list, `pop()` removes and returns an item at a specific index (default is the last item), and `remove()` removes the first occurrence of a specified value from the list.")

# Write a code to reverse only the vowels in a string.
def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    s_list = list(s)
    left, right = 0, len(s_list) - 1
    
    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
            
    return ''.join(s_list)

s = "hello world"
print(reverse_vowels(s))

# How do you check if a list contains all unique elements? Write efficient code

def has_unique_elements(lst):
    return len(lst) == len(set(lst))    
lst = [1, 2, 3, 4, 5]
print(has_unique_elements(lst))

# Write a function to check if two strings are anagrams.

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2) 

str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))


# Explain how tuple immutability is bypassed using object references.

print(f"Tuple immutability can be bypassed by using mutable objects like lists or dictionaries as elements within a tuple. While the tuple itself cannot be modified, the mutable objects it contains can be changed.")


t = (1, [2, 3], 4)  
t[1].append(5) 
print(t)  


# Write a program to remove all punctuation from a string.

import string
def remove_punctuation(s):  
    return s.translate(str.maketrans('', '', string.punctuation))   
s = "Hello, world! This is a test string with punctuation."
print(remove_punctuation(s))

# Given a list of integers, find the first pair whose sum is a target value using hashing.
def find_pair_with_sum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None
nums = [10, 15, 3, 7]
target = 17
print(find_pair_with_sum(nums, target))


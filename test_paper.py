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

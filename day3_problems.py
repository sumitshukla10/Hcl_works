#Day3 of problem solving - Sumit Shukla

# 1. Write a program to check if a number is positive, negative, or zero using if…elif…else.

num=int(input("Enter your number : "))

if num>0:
    print(f"Entered number {num} is positive")
elif num<0:
    print(f"Entered number {num} is negative")
else:
    print(f"Entered number is {num} zero")

# 2. Write a program to print numbers from 1 to 10 using a while loop.

#using for loop

for i in range(1,11):
    print(i,end=" ")

print("\n")
i=1
while i<=10:
    print(i,end=" ")
    i+=1

# 3. Write a program using a for loop to print the elements of a list.

fav_destinations=["Bali","Debai","Switzerland","pattaya"]

for i in fav_destinations:
    print(i)

# 4. Write a program to demonstrate an infinite loop with a while True and break after 5 iterations.

count=0
while True:
    print("Infinite Loop ",count+1)
    count+=1
    if count==5:
        break

# 5. Create a nested loop that prints a 3x3 grid of *.

for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()

# 6. Use the continue statement to skip even numbers from 1 to 10.

for i in range(1,11):
    if i%2==0:
        continue
    else:
        print(i,end=" ")

print("\n")

# 7. Write a function that uses assert to check if a number is positive.

def number_checker(num):
    assert num>0,"Number is not positive"
    print("The number is positive")

number_checker(12)

# 8. Use a match-case to simulate a simple calculator (add, subtract, multiply).

a=float(input("Enter first number : "))
b=float(input("Enter your second number : "))

choose=input("Choose operations accordingly + - * / ")

match choose:
    case "+":
        print(f"The addition of two number {a} , {b} is {a+b}")
    case "-":
        print(f"The subtraction of two number {a} , {b} is {a-b}")
    case "*":
        print(f"The multiplication of two number {a} , {b} is {a*b}")
    case _:
        print("Invalid opeartion is choosen")

# 9. Use the pass statement in a placeholder function called process().

def process():
    pass

process()

# 10. Write Python code to print the following pattern:

for i in range(1,6):
    print("*"*i)

print("\n")

for i in range(5,0,-1):
    print("#"*i)

print("\n")

rows = 5
for i in range(rows):
    spaces = " " * (rows - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
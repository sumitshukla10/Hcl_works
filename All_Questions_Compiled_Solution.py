print("This is a compiled file for the Assignment Question - during Training Submitted by SUMIT SHUKLA")

''' 30th June Questions'''

print("calculate sum function")
def calculate_sum(n):
    sum=0
    for i in range(n+1):
        if i%3==0 or i%5==0: 
            sum+=i
    return sum

n=int(input("Enter the value of n:"))
print(f"the sum of number {n} divisible are by 3 or 5 is :{calculate_sum(n)}")


print("problem 2 sum of squares")

def calculate_difference(n):
    sum=0
    square_sum=0
    for i in range(1,n+1):
        sum+=i
    for i in range(1,n+1):
        square_sum=(square_sum)+(i**2)

    return square_sum-sum

num=int(input("Enter the value of num"))
print(f"sum of diff of squares of first {num} natural numbers are :{calculate_difference(num)}")


print("problem 3 checking weather a number is increasing num")

num3=input("Enter the value of num3")
isIncreasing=True

for i in range(len(num3)-1):
    if num3[i]>=num3[i+1]:
        isIncreasing=False
        break
print(f"Entered number {num3} is increasing or not :{isIncreasing}")

#Problem 4

print(f"Method for checking a number is a power of 2 or not")
num4=int(input("enter the value of num4"))

def check_power_two(num4):
    if num4<=0:
        print("Enter a valid Number")
    while num4%2==0:
        num4=num4//2
    return num4==1
print("Entered number is in power of two")

print(f"check weather a number {num4} is power of two or not :{check_power_two(num4)}")

#Problem 4
print("Solution to question 5")
myArray=[3,5,2,8,10,12,43,24]
print(sorted(myArray))
newArray=[]
for i in myArray:
    newArray.append(sorted(myArray))

print(newArray[1])
    
    
'''JULY 1st ASSIGNMENT QUESTIONS'''

print("Problem statement 1 ")
num_range=int(input("Enter the range"))
nums=[]
for i in range(1,num_range+1,1):
    num=int(input("Enter the num value"))
    nums.append(num)
print(nums)
sum=0
for i in nums:
    sum+=i
print(sum)

print(f"problem statemnet 2 ")

num2=int(input("enter the range for num2"))
nums2=[]
for i in range(1,num2+1,1):
    num2=int(input("Enter the value of num2"))
    nums2.append(num2)
max_element=nums2[0]
min_element=nums2[0]

maxi=[]
min=[]
for i in nums2:
    if i>max_element:
        max_element=i
        maxi.append(max_element)
for i in nums2:
    if i<min_element:
        min_element=i
        min_element.append(min_element)
print(f"Maximum element is {maxi} and minimum elements is {min}")

print("Problem statement 3")
num3=int(input("Enter the range of num3"))
nums3=[]
for i in range(1,num3+1,1):
    num=int(input("Enter the values"))
    nums3.append(num)

print(nums3)

rev_array=[]
for i in range(len(nums3)-1,-1,-1):
    rev_array.append(nums3[i])

print(rev_array)

print("Problem statement 4")

num4=int(input("Enter the number 30"))
marks=[]
for i in range(1,num4+1,1):
    num=int(input("Enter the vlaue of marks"))
    marks.append(num)


print(marks)
count=[0]*101
for i in marks:
    if 0<=i<=100:
        count[i]+=1

for i in range(101):
    if count[i]>0:
        print(f"{i}:{count[i]}",end=" ")


print("Problem statement 5")

# Factorial problem

print("Factorial of given number n")
print("Problem statement 6")
def factorial(n):
    fact=0
    if(n==0):
        return 1
    else:
        fact=n*factorial(n-1)
    return fact

n=int(input("Enter a value : "))
print(f"Factorial of given number {n} is : {factorial(n)}")

# problem statement 7 averrage of given n number

number=int(input("Enter the number"))
avg=[]
for i in range(1,number+1,1):
    num=int(input("Enter the vbalue of number : "))
    avg.append(num)
print(avg)

print("Calculating the average of given numbers")
sum=0
for i in avg:
    print(i)
    sum=sum+i
print(f"Average of given numbers is {sum//len(avg)} ")

# Problem statement 8 Train problem

def train_length(x,y):
     len=((x*1000)/3600)*y
     return len

x=int(input("Enter the value of x : "))
y=int(input("Enter the value of y : "))
if x<=0 or y<=0:
    print("Enter the positive values for the x and y ")
else:
    print(f"Length of the train is : {train_length(x,y)}")

# Problem statement 9  Speed of the Train

def speed_of_train(x,y,speed):
    speedOfTrain=((x/y)+(25/18))*18/5
    return speedOfTrain

x=int(input("Enter the length of the train : "))
y=int(input("Enter the train passing time in seconds : "))
speed=int(input("Enter the speed of the train  :"))

if x<=0 or y<=0 or speed<=0:
    print("Enter the correct value for the x y and speed ")
else:
    print(f"The Speed of the train is : {speed_of_train(x,y,speed)}")

a="a2b3cd4"
sum=0
for i in a:
    if i.isdigit():
        #print(i)
        sum=sum+int(i)

print(f"the sum of digits present in the string is : {sum}")
        

str="a2b3c4"
res=""
for i in range(len(str)):
    if str[i].isdigit():
        res+=str[i-1]*int(str[i])
print(f"the repetititon of characters based on digits : {res}")

# Activity 10 ---> two goods train running in opposite direction

print("Goods Train Problem")

def slowTrain(len,x,y):
    print(f"The speed of the faster train is : {x} and speed of slower train is : {y}")
    relative_speeds=(x+y)*5/18 # to convert them into m/s
    time=len/relative_speeds
    time=round(time)
    return time

    

length_of_train=int(input("Enter the Length of the Train : say 500 : "))
x=int(input(f"Enter the speed of the first train : say 45 "))
y=int(input(f"Enter the speed of the second train : say 30 "))

if x<=0 or y<=0:
    print(f"Please Enter the correct values for the x and : {x}{y}")
else:
    print(f"Time Taken by the slower train to pass the faster train is : {slowTrain(length_of_train,x,y)} seconds")


# Activity 11 length of the Reactangular Park

def area(s,t,x,y):
    speed=s*(1000/60)
    perimeter=speed*t
    dist=perimeter/(2*(x+y))
    length=x*dist
    breadth=y*dist
    area=length*breadth
    area=round(area)
    return area

print("Length of the rectangular park problem : ")
speed=int(input("Enter the speed say 12 km/hr : "))
time=int(input("Enter the time say 8 minutes : "))
x,y=(3,2)

if speed<=0 or time<=0:
    print("Entered values are not correct")
else:
    print(f"The area of rectangle is : {area(speed,time,x,y)} sq/m")

# Activity 12 sum of square 

import math
def sumOfThree(product,sum):
    res=math.sqrt(product+(2*sum))
    res=round(res)
    return res
    
    
print("Sum of square of given three numbers")
product=int(input("Enter the sum of squares three numbers : say 138 "))
sum=int(input("Enter the sum of given three numbers : say 131 "))

if sum<=0 or product<=0:
    print("Enter the valid values for x y and z ")
else:
    print(f"The sum of given three numbers  is : {sumOfThree(product,sum)}")

#Problem statement 13 
print("Amount of B problem statement")
amount=int(input("Enter the total amount of A and B : say 1210 "))
amount_of_B=(amount*4)/6
amount_of_B=round(amount_of_B)
print(f"The amount of B is : {amount_of_B}")

# Activity 15 choose the operation and perform it 

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

'''JULY 3rd ASSIGNMENT QUESTIONS'''

print("Program to create tuple of 5 numbers : ")

num=int(input("Enter the range of num : "))
nums=[]
tups=()
for i in range(num):
    n=int(input("Enter the value of n : "))
    nums.append(n)

#print(nums)

for n in nums:
    tups=tups+(n,)

print(tups)

print(f"Length of the tupe is : {len(tups)}")
print(f"First value of the tuple is : {tups[0]}")
print(f"Last value of the tuple is : {tups[len(tups)-1]}")
# print(f"Mid value of the tuple is : {tups[2]}")
length=len(tups)
if length%2==0:
    print(tups[(length//2)-1])
    print(tups[length//2])
else:
    print(tups[length//2])


#Problem statement 3 : printing tuple inside tuple

print("Tuple containing other tuple")
tups=(2,4,(1,3,5,7,9,10),100,200)
innerTuple=tups[2]
print(f"Inner tuple elements are : {innerTuple}")

for tup in innerTuple:
    print(tup,end=" ")

# Problem statement 4 - input a list from user and convert to tuple

print("Input LIST from user and convert it to a tuple ")
n=int(input("Enter the range of the List : "))
myList=[]

for i in range(n):
    num=int(input("Enter the value of num to be added in myList : "))
    myList.append(num)

print(f"Values present in the list is : {myList} and type of myList is {type(myList)}")

print(f"Converting List to Tuple")

myTuple=tuple(myList)

print(f"Values present in myTuple is {myTuple} and type of myTuple is {type(myTuple)}")

# Problem assessment 5 - raise execption while changing the tuple value

print("Raise execption while changing the tuple value")

myTup=(2,3,4,5,6,7,8,9,0)
try:
    myTup[2]=200
except:
    print("Error Occurred while changing the value of Tuple")
else:
    print("Happy coding")
finally:
    print("Here Your code ends")

# Problem statement 6 - In list taking 5 students name and display it

print("In list taking 5 students name and display it")
myNames=[]
for i in range(1,6):
    name=input("Enter your name")
    myNames.append(name)
print(f"Names present in the List are : {myNames}")

# problem statement 7 - Replacing 3rd value of the list :

print("Replacing 3rd value of the list")

myValues=[2,4,6,8,10]
for i in range(len(myValues)):
    if i==3:
        myValues[i]=100
    else:
        continue
print(myValues)
    
# Problem statememnt 16 - printing keys and values of dictionary 

print("printing keys and values of dictionary")
myDict={"name":"sumit","age":22,"id":52336999}

for key,values in myDict.items():
    print(key,":",values)

# Problem statement 15 - Removing a key from the dictionary 

print("Removing a key from the dictionary")
dict={"name":"sumit","age":22,"id":52336999}
print(f"Before deleting dict is : {dict}")

del dict["age"]
print(f"After deleting a key from dict : {dict}")

#problem statement 14 adding new key value pair in existing dictionary

print("adding new key value pair in existing dictionary")
dict2={"name":"sumit","age":22,"id":52336999}
dict2["Nationality"]="Indian"

print("After adding a key value in dict2 ",dict2)

#problem statement 13 from student marks dictionary showing the marksno

print("from student marks dictionary showing the marks")
student_mark={"sumit":95,"Amit":76,"Rahul":49,"Akash":98}
for i in student_mark:
    print(f"marks of particular student are : {student_mark[i]}")

# 20 Removing duplicates from the list using set

print("Removing duplicates from the list using set")
lst=[2,2,3,5,6,7,8,9,10]
mySet=set()
for num in lst:
    print(num)
    mySet.add(num)
print(f"The element present in the set are : {mySet}")

#21 Check weather a given element is present in the set or not

print("Check weather a given element is present in the set or not")
mySet=(2,4,5,6,7,8,9,10)
num=int(input("Enter a value of num is between 0 to 10 : "))

if num in mySet:
    print(f"{num} is present in the given set")
else:
    print(f"{num} is not present in the set")

# 22 pop elements from set until it is empty

print("pop elements from set until it is empty")
mySet={2,3,4,5,6,7,8,9}
while mySet:
    mySet.pop()
print(f"After removing all the element : {mySet}")

# 12 Input a sentence . split into words and rejoin it

print("Input a sentence . split into words and rejoin it")
str=input("Enter a sentence : ")
print(str.split())
print("-".join(str))

'''PRACTICE QUESTIONS'''

#swapping three numbers
a=10
b=20
c=30
temp=a
a=c
c=b
b=temp

print("a is :",a)

print("b is :",b)

print("c is :",c)


print("swapped numbers are : ",a,b,c)

print("a =",a , "b =",b , "c =" ,c)

#Activity 2 - is student pass or not


marks=[32,38,99]
count=0
for student in marks:
    if student>=35:
        count+=1
print("number of passed students ",count)


#Activity 3

nums=[-6,10,3,-7,12,-9]
negativeNumCount=0
positiveNumCount=0

for num in nums:
    if num>=0:
        positiveNumCount +=1
    else:
        negativeNumCount +=1
print("Number of positives in nums is :",positiveNumCount , "and" , "Number of negative in nums is ",negativeNumCount)

#Activity 4 even or odd

print("Checking odd and even number")

num = int(input("Enter a number"))

if num%2==0:
    print("Entered number is even")
else:
    print("Entered number is odd")

# activity 5 adding 3 numbers
print("Adding three numbers ")

def addThreeNumbers(a,b,c):
    return a+b+c

print("Sum of three numbers is :", addThreeNumbers(10,20,30))

#Activity 6  Count number of digits

print("counting the number of number")

numDigit=int(input("enter a number"))
count=0

if numDigit==0:
    count=1
else:
    numDigit=abs(numDigit)

while numDigit:
    count+=1
    numDigit//=10

print("Number of digit is:",count)

#Activity 7  sum of all  the digits

print("Sum of all the digits")
n=int(input("Enter a number for sum calculation"))
sum=0
n=abs(n)

while n:
    digit=n%10
    sum+=digit
    n=n//10
print("Submission of digits entered", sum)

#Activity 8  decimal to binary representation
print("Decimal to binary representation")

num2=5
ans=''

while num2>0:
    ans=str(num2&1)+ans
    num2>>=1
print("Binary is",ans)

#Activity 9 binary to decimal

print("Binary to decimal")

binNumber="1010"
itr=0
res=0
while binNumber:
    digit=binNumber[-1]
    if digit=='1':
        res+=2**itr
    itr+=1
    binNumber=binNumber[:-1]

print("decimal number is:",res)





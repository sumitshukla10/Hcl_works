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
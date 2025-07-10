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
    
    

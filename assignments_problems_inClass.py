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



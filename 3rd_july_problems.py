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


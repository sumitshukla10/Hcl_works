# 1. Write a Python program that prints numbers from 1 to 5 using a single thread. Explain how single-threaded execution flows in your code.

import time 

def print_numbers():
    for i in range(1,11):
        print(f"Numbers are {i}")
        time.sleep(2)

print_numbers()

# 2. Write a program using threading to simulate downloading two files simultaneously. Show how Python can multitask using threads.

def function_to_download_file(file_name):
    print(f"file downloading starts : {file_name}")

    for i in range(1,6):
        print(f"Downloading ffile {file_name} : {i*20}%")
    print(f"Downloading finished : {file_name}")

function_to_download_file("file1")
function_to_download_file("file2")

# Write a Python program to create and start three threads. Each thread should print a message like "Thread 1 running...". Use the threading.Thread class.

import threading

def helper(n):
    print(f"Thread number {n} is running ")

threads=[]
for i in range(1,4):
    t=threading.Thread(target=helper,args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

# 3. Write one example using threading.Thread and another using multiprocessing.Process. Compare their memory sharing behavior in your explanation.

import threading
import time

def func_to_download(file):
    print(f"File downloading start : ")
    for i in range(1,6):
        time.sleep(1)
        print(f"{file} {i*20}%")
    print(f"File downloading finishes ")

f1=threading.Thread(target=func_to_download,args=("file1,"))
f2=threading.Thread(target=func_to_download,args=("file2,"))

f1.start()
f2.start()

f1.join()
f2.join()
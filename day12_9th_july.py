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

# Write a multithreaded Python program where threads perform CPU-bound tasks (e.g., calculating factorial). Observe and explain how the Global Interpreter Lock (GIL) affects performance.

import threading
import time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def calculate_factorial(num):
    print(f"Calculating factorial of {num}")
    result = factorial(num)
    print(f"Factorial of {num} is {result}")

threads = []
for i in range(5, 10):
    t = threading.Thread(target=calculate_factorial, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()    
      


# 5. Write a program that performs two I/O tasks (e.g., writing to a file and downloading a webpage) using threads. Explain why threads are useful here.
import threading
import requests 
import time
def write_to_file():
    with open("output.txt", "w") as f:
        for i in range(5):
            f.write(f"Line {i+1}\n")
            time.sleep(1)
    print("File writing completed.")
def download_webpage():
    url = "https://www.google.com"
    response = requests.get(url)
    print(f"Downloaded webpage content: {response.text[:100]}...")
    print("Webpage download completed.")

# 6. Write a Python program to create and start three threads. Each thread should print a message like "Thread 1 running...". Use the threading.Thread class.
threads = []
for i in range(1, 4):   
    t = threading.Thread(target=lambda n=i: print(f"Thread {n} running..."))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

# 7. Create a program with two threads. Use .start(), .is_alive(), and .join() methods, and explain how these control thread execution.
# 
import threading
import time 
def thread_function(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} finishing")
thread1 = threading.Thread(target=thread_function, args=(1,))
thread2 = threading.Thread(target=thread_function, args=(2,))
thread1.start() 
thread2.start()
print(f"Thread 1 is alive: {thread1.is_alive()}")
print(f"Thread 2 is alive: {thread2.is_alive()}")
thread1.join()
thread2.join()

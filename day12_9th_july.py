# 1. Write a Python program that prints numbers from 1 to 5 using a single thread. Explain how single-threaded execution flows in your code.

import time 

def print_numbers():
    for i in range(1,11):
        print(f"Numbers are {i}")
        time.sleep(2)

print_numbers()

# 2. Write a program using threading to simulate downloading two files simultaneously. Show how Python can multitask using threads.
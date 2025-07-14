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
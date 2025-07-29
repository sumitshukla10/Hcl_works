# Stack - data structure where elments are stored in LIFO order , stack has functions like empty(),size(),push(),pop(),top()/peek()

# In Python a stack can be implemented in three following ways : -
# list
# Collections.deques
# queue.LifoQueue

# Implementation using list: Instead of push(), append() is used to add elements to the top of the stack while pop() removes the element in LIFO order. 

stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

stack.pop()
print(stack) #last element will get removed

# Implementation using collections.deque:

from collections import deque

stack2=deque()
stack2.append(100)
stack2.append(200)
stack2.append(300)

print(stack2)

#popping of elementg
stack2.pop()
print(stack2)

# Implementation using queue module - Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function and get() takes data out from the Queue. 
# There are various functions - maxsize , empty() , full() , get() , get_nowait() , put(item) , put_nowait(item)

from queue import LifoQueue

stack3=LifoQueue(maxsize=3)

print(stack3.qsize()) # returns 0 as stack3e is empty now

stack3.put('a')
stack3.put('b')
stack3.put('c')

print(stack3.full())
print(stack3.qsize())

print(stack3.get())
print(stack3.get())
print(stack3.get())

print(stack3.empty())

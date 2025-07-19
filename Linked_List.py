#Linked LIst - > for finding the mid node of the LL using noive approach and slow/fast tortoise algo approach


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def getLength(head):
    length=0
    curr=head
    while curr:
        length+=1
        curr=curr.next
    return length
def midNode(head):
    curr=head
    len=getLength(head)
    mid=len//2
    while mid:
        curr=curr.next
        mid-=1
    return curr.data

def getMidNode_using_tortoise(head):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        fast=fast.next.next
        slow=slow.next
    return slow.data

def reverseLinkedList(head):
    curr=head
    prev=None
    while curr is not None:
        nextNode=curr.next
        curr.next=prev
        prev=curr
        curr=nextNode
    return prev

def reverse_linked_list_recursive(head):
    if head is None or head.next is None:
        return head
    
    lst=reverse_linked_list_recursive(head.next)
    head.next.next=head
    head.next=None
    return lst

def reverse_linked_list_using_stack(head):
    stack=[] # initialise an empty list to store the list elements

    temp=head
    while temp.next is not None:
        stack.append(temp)
        temp=temp.next

    head=temp

    while stack:
        temp.next=stack.pop()
        temp=temp.next

    temp.next=None
    return head



def print_linked_list(head):
    curr=head
    while curr is not None:
        print(curr.data)
        curr=curr.next
    print()    


def main():
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    head.next.next.next.next=Node(50)
    print(midNode(head))
    print("\n")
    print(getMidNode_using_tortoise(head))
    print("\n")

    print_linked_list(head)
    head=reverseLinkedList(head)
    print_linked_list(head)
    head=reverse_linked_list_recursive(head)
    print(f"recursively printing the linked list : {print_linked_list(head)}")

if __name__=='__main__':
    main()




#Reversing the Linked List -> time o(n) and space O(1)
# The idea is to reverse the links of all nodes using three pointers: 
# prev: pointer to keep track of the previous node
# curr: pointer to keep track of the current node 
# next: pointer to keep track of the next node
# Starting from the first node, initialize curr with the head of linked list and next with the next node of curr. Update the next pointer of curr with prev. Finally, move the three pointer by updating prev with curr and curr with next.

# --------------------------------------

# [Alternate Approach - 1] Using Recursion - O(n) Time and O(n) Space
# The idea is to reach the last node of the linked list using recursion then start reversing the linked list from the last node.

# Divide the list in two parts - first node and rest of the linked list.
# Call reverse for the rest of the linked list.
# Link the rest linked list to first.
# Fix head pointer to NULL.

# [Alternate Approach - 2] Using Stack - O(n) Time and O(n) Space
# The idea is to traverse the linked list and push all nodes except the last node into the stack. Make the last node as the new head of the reversed linked list. Now, start popping the element and append each node to the reversed Linked List. Finally, return the head of the reversed linked list.

# Push all the nodes(values and address) except the last node in the stack.
# Once the nodes are pushed, update the Head pointer to the last node.
# Start popping the nodes and push them at the end of the linked list in the same order until the stack is empty.
# Update the next pointer of last node in the stack by NULL.

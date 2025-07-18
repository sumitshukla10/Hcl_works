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

if __name__=='__main__':
    main()




#Reversing the Linked List -> The idea is to reverse the links of all nodes using three pointers: 
# prev: pointer to keep track of the previous node
# curr: pointer to keep track of the current node 
# next: pointer to keep track of the next node
# Starting from the first node, initialize curr with the head of linked list and next with the next node of curr. Update the next pointer of curr with prev. Finally, move the three pointer by updating prev with curr and curr with next.


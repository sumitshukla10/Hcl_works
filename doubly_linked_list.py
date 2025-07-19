class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

# [Naive Approach] Using Recursion - O(n) Time and O(n) Space
# The idea of the recursive code is simple,

# Swap the next and previous pointers (or references) of the current node.
# Recursively call for the remaining list (We mainly need to call for curr->prev as previous now hold the earlier next node).

def recursive_reverse(curr):
    if curr is None:
        return None
    temp=curr.prev
    curr.prev=curr.next
    curr.next=temp

    if curr.prev is None:
        return curr
    
    return recursive_reverse(curr.prev)

# [Expected Approach] Using Two Pointers - O(n) Time and O(1) Space
# The idea is to reverse doubly linked list using two pointers for traversing through the list and swapping the next and previous pointers of every two consecutive nodes. 

# Step-by-step algorithm:

# Initially, prevNode is set to NULL and currNode starts at the head.
# As the list is traversed,
# Swap the currNode->next and currNode->prev
# Move currNode to the next node, currNode = currNode->prev.
# After traversing all the nodes, prevNode will point to the second node of the reversed list, so update the previous pointer of prevNode as the new head of the linked list, head = prevNode->prev and return it.

def recursive_reverse_way_two(head):
    if head is None or head.next is None:
        return head
    
    prevNode=None
    currNode=head

    while currNode is not None:
        prevNode=currNode.next
        currNode.prev=currNode.next
        currNode.next=prevNode

        currNode=currNode.prev

def print_linked_list(node):
    while node is not None:
        print(node.data,end=" ")
        node=node.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    print("Original Linked List")
    print_linked_list(head)
    head=recursive_reverse(head)
    print("Reversed Linked List")
    print_linked_list(head)
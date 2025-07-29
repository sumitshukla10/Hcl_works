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


#     Given a string containing of length N , find the length of the maixmal palindrome formed from the string

# The maximal palindrome can be formed as follows:

# Say we are given the string : "abdbcda" . The length of the maximal palindrome will be 4 since the maximal palindrome will be abba  or adda.

# We can form a palindrome by "linking up the characters at any two indices : if we have the maixmal palindrome as "abba" from the string "abdbcda" we link up the 'a' s at index 0 and at index 6

# The we nest that linking by linking the 'b' s at index 2 and index 3. (NOTE: 0-based indexing is used here) 

# Note that we form the palindrome by nesting links and we cannot have any links crossing each other. So from the string "abdbcda" the palindrome "abddba" is not valid since the links for d and the links for b "cross each other"  . More formally two links between indices i1 and i2 and between j1 and j2 are said to cross when either   j1<i1<j2<i2 or i1<j1<i2<j2 . A maximal palindrome is the palindrome of maximum length formed by nesting these links

# Report the length of the largest maximal palindrome.  


# Input Description:
# The first and only line of input contains a string of at most 1000 characters

# Output Description:
# Output a single number : the length of the maximal palindrome formed. We can prove that this length is at least 1 .

# Sample Input :
# abddba
# Sample Output :
# 4

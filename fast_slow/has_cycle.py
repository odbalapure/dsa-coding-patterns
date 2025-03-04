from Node import *

def has_cycle_brute(head: LinkedListNode) -> bool:
    """
    Does a linked list have cycle
    :head LinkedListNode: Head of linked list using a hashset
    :return: bool

    COMPLEXITY
    Time: O(n); since we traverse the entire linked list
    Space: O(n); in worst case we are storing every node in the linked list in the hashset
    """
    st = set()
    temp: LinkedListNode = head
    while temp:
        if temp in st:
            return True
        st.add(temp)
        temp = temp.next
    return False

def has_cycle(head: LinkedListNode) -> bool:
    """
    Does a linked list have cycle
    :head LinkedListNode: Head of linked list using two pointers
    :return: bool

    COMPLEXITY
    Time: O(n); n is the no. of nodes in the linked list
    Space: O(1) 
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

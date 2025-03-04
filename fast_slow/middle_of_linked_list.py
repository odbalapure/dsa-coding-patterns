from Node import *

def middle_of_linked_list(head: LinkedListNode) -> LinkedListNode:
    """
    Find middle of a linkedlist
    :head LinkedListNode: Head of linked list
    :return: LinkedListNode
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

from Node import *

def has_cycle(head: LinkedListNode) -> bool:
    """
    Does a linked list have cycle
    :head LinkedListNode: Head of linked list
    :return: bool
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

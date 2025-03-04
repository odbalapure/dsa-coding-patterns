from Node import *
from typing import Tuple

def createList(head: LinkedListNode) -> Tuple[list, int]:
    temp: LinkedListNode = head
    arr: list = []
    while temp:
        arr.append(temp)
        temp = temp.next
    return (arr, len(arr))
        
def middle_of_linked_list_brute(head: LinkedListNode) -> LinkedListNode:
    """
    Find middle of a linkedlist
    :head LinkedListNode: Head of linked list
    :return: LinkedListNode

    COMPLEXITY
    Time: O(n); since we iterate over each node
    Space: O(n); since we are storing each node
    """
    arr, n = createList(head)
    return arr[n//2]

def middle_of_linked_list(head: LinkedListNode) -> LinkedListNode:
    """
    Find middle of a linkedlist
    :head LinkedListNode: Head of linked list
    :return: LinkedListNode

    COMPLEXITY
    Time: O(n); since we iterate over each node
    Space: O(n); since we are storing each node
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

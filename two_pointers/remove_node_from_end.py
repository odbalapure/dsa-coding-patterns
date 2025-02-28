def remove_nth_from_end(head, n):
    """
    Remove nth from the end
    :head LinkedListNode: LL node
    :n int: Length of the LL
    :return: LinkedListNode
    """
    slow = fast = head
    
    for _ in range(n):
        fast = fast.next
    
    if not fast:
        return head.next
    
    while fast.next:
        fast, slow = fast.next, slow.next
    
    slow.next = slow.next.next

    return head

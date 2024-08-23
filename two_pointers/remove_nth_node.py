def remove_nth_node(head, n: int):
    """
    Remove nth node from the nth of linked list
    :head: Head of linkedlist
    :n: Nth value from end
    :return: Head of linkedlist
    """
    right = left = head

    for _ in range(n):
        right = right.next

    if not right:
        return head.next

    while right.next:
        right = right.next
        slow = slow.next
    
    left.next = left.next.next

    return head
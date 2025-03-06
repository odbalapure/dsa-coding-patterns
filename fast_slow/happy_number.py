def get_sum_square_digit(num: int) -> bool:
    total = 0
    while num:
        num, digit = divmod(num, 10)
        total += digit * digit
    return total

def is_happy_number(num: int) -> bool:
    """
    Check if number is a happy number
    If the square of its digits add up to 1, then its happy
    Else if it reaches a cycle then its not happy
    :param num: Input number
    :return: bool

    COMPLEXITY
    Time: O(logn)
    Space: O(logn)
    """
    sq_set = set()
    while num != 1 and num not in sq_set:
        sq_set.add(num)
        num = get_sum_square_digit(num)
    return num == 1
    
def is_happy_number(num: int) -> bool:
    """
    Check if number is a happy number
    If the square of its digits add up to 1, then its happy
    Else if it reaches a cycle then its not happy
    :param num: Input number
    :return: bool

    COMPLEXITY
    Time: O(logn)
    Space: O(1)
    """
    slow, fast = num, get_sum_square_digit(num)
    while fast != 1 and slow != fast:
        slow = get_sum_square_digit(slow)
        fast = get_sum_square_digit(get_sum_square_digit(fast))
    return fast == 1

print(is_happy_number(7))

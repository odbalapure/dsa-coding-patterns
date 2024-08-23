def valid_palindrome(string: str) -> bool:
    """
    Check for valid palindrome
    :str: String
    :bool: Flag indicatin is palindrome
    """
    left, right = 0, len(string) - 1
    while left < right:
        if (string[left] != string[right]):
            return False
        left = left + 1
        right = right - 1
    return True
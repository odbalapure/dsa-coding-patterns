def is_valid_palindrome(string: str) -> bool:
    """
    Check for valid palindrome
    :string str: Input string
    :return: bool
    """
    string = ''.join(char for char in string if char.isalnum()).lower()
    low, high = 0, len(string) - 1
    while low <= high:
        if string[low] != string[high]:
            return False
        low, high = low + 1, high - 1
    return True

print(is_valid_palindrome("kayak"))

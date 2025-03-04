def is_valid_palindrome_brute(string: str) -> bool:
    """
    Check for valid palindrome
    :string str: Input string
    :return: bool

    COMPLEXITY
    Time: O(2n) =~ O(n); since two iterations are performed
    Space: O(n); since we are creating a copy of original string
    """
    string = "".join(ch for ch in string if ch.isalnum()).lower()
    reverse_string = string[::-1]
    return reverse_string == string

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

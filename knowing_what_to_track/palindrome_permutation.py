def palindrome_partition_brute(st: str) -> bool:
    """
    Check if a palindrome partition is possible by generating all permutations.

    COMPLEXITY
    Time: O(n! * n), where n is the length of the string. Generating permutations takes O(n!) time, 
          and checking each permutation for palindromicity takes O(n) time.
    Space: O(n * n!), where n! is the number of permutations and each permutation is of length n.

    :param st: Input string
    :return: Boolean flag indicating whether a palindrome partition is possible
    """
    perms = custom_permutations(st)
    for perm in perms:
        left, right = 0, len(perm) - 1
        while left < right:
            if perm[left] != perm[right]:
                break
            left += 1
            right -= 1
        else:
            return True
    return False

def custom_permutations(s: str) -> list:
    """
    Generate all permutations of a given string.

    :param s: Input string
    :return: List of all permutations of the input string
    """
    if len(s) == 1:
        return [s]
    perms = []
    for i, char in enumerate(s):
        remaining_string = s[:i] + s[i+1:]
        for p in custom_permutations(remaining_string):
            perms.append(char + p)
    return perms

print(palindrome_partition_brute('abab')) # True
print(palindrome_partition_brute('peas')) # False

def palindrome_partition(st: str) -> bool:
    """
    Check if a palindrome partition is possible using character frequency.

    COMPLEXITY
    Time: O(n), where n is the length of the string. Counting character frequencies and then checking
          the number of odd frequencies are both linear time operations.
    Space: O(1), since the number of distinct characters is bounded (e.g., 26 for English lowercase letters).

    :param st: Input string
    :return: Boolean flag indicating whether a palindrome partition is possible
    """
    freq = {}
    for char in st:
        freq[char] = freq.get(char, 0) + 1
    
    count = 0
    for freq_count in freq.values():
        if freq_count % 2:
            count += 1

    return count <= 1

print(palindrome_partition('abab')) # True
print(palindrome_partition('peas')) # False
def can_construct(ransome_note: str, magazine: str) -> bool:
    """
    Check if ransom_note can be constructed using the letters from magazine

    COMPLEXITY
    Time: O(m + n)
    Space: O(1)

    :ransome_note: str
    :magazine: str

    Return true if it can be constructed
    """
    magazine_count: dict = {}
    for char in magazine:
        magazine_count[char] = magazine_count.get(char, 0) + 1

    for char in ransome_note:
        if char in magazine_count and magazine_count[char] > 0:
            magazine_count[char] -= 1
        else:
            return False

    return True

print(can_construct('program', 'programming')) # True
print(can_construct('codinginterviewquestions', 'aboincsdefoetingvqtniewonoregessnutins')) # True
print(can_construct('code', 'coingd')) # False
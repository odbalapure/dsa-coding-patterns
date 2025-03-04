def sort_colors(colors: list[int]) -> None:
    """
    Sort a list of 0, 1, 1
    :colors list: List of integers
    :return: None

    COMPLEXITY
    Time: O(n)
    Space: O(n)
    """
    zero = one = two = 0
    for num in colors:
        if num == 0:
            zero += 1
        elif num == 1:
            one += 1
        else:
            two += 1
    colors[:zero] = [0] * zero
    colors[zero:zero+one] = [1] * one
    colors[zero+one:] = [2] * two

def sort_colors(colors: list) -> None:
    """
    Sort a list of 0, 1, 1
    :colors list: List of integers
    :return: None

    COMPLEXITY
    Time: O(n)
    Space: O(1)
    """
    start, current, end = 0, 0, len(colors) - 1
    while current <= end:
        if colors[current] == 0:
            colors[start], colors[current] = colors[current], colors[start]
            start, current = start + 1, current + 1
        elif colors[current] == 1:
            current += 1
        else:
            colors[current], colors[end] = colors[end], colors[current]
            end -= 1

colors = [0, 1, 0, 2, 0, 0, 1, 2]
sort_colors(colors)
print(colors)

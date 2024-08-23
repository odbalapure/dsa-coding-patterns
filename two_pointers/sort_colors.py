def sort_colors(colors: list[int]) -> list[int]:
    """
    Sort an array of 0, 1, 2
    :colors: List of numbers
    :return: Sorted array
    """
    start, current, end = 0, 0, len(colors) - 1
    while current <= end:
        if colors[current] == 0:
            colors[start], colors[current] = colors[current], colors[start]
            current += 1
            start += 1
        elif colors[current] == 1:
            colors[current] = 1
            current += 1
        else:
            colors[end], colors[current] = colors[current], colors[end]
            end -= 1
    return colors
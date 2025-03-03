def sort_colors(colors: list) -> None:
    """
    Sort a list of 0, 1, 1
    :colors list: List of integers
    :return: None
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

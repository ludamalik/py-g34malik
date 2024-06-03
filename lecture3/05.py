def roll(lst, n):
    part1 = lst[-n:]

    part2 = lst[:-n]

    return part1 + part2
n = 2
result1 = roll([1, 2, 3, 4, 5], n)
print(result1)
n = -2
result2 = roll([1, 2, 3, 4, 5], n)
print(result2)
def max_n(lst, n):

    sorted_lst = sorted(lst, reverse=True)

    return sorted_lst[:n]

result1 = max_n([1, 2, 3], 1)
print(result1)

result2 = max_n([1, 2, 3], 2)
print(result2)

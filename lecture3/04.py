def includes_any(lst, values):

    for value in values:

        if value in lst:
            return True

    return False

result1 = includes_any([1, 2, 3, 4], [2, 9])
print(result1)

result2 = includes_any([1, 2, 3, 4], [8, 9])
print(result2)

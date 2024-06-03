def every_nth(lst, n):
    return lst[n-1::n]
list = [1, 2, 3, 4, 5, 6]
n = 2
result = every_nth(list, n)
print(result)

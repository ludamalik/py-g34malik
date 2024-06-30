def average_by(lst, fn=lambda x: x):
    if not lst:
        raise ValueError("The list must contain at least one element")
    mapped_values = list(map(fn, lst))
    return sum(mapped_values) / len(mapped_values)

lst = [{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }]
print(average_by(lst, lambda x: x['n']))
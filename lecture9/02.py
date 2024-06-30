def sum_by(lst, fn):
    mapped_values = map(fn, lst)
    return sum(mapped_values)

data = [{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }]
result = sum_by(data, lambda v: v['n'])
print(result) 
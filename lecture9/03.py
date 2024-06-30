def sort_by_indexes(a, b, reverse=False):
    combined = list(zip(a, b))
    sorted_combined = sorted(combined, key=lambda x: x[1], reverse=reverse)
    sorted_a = [x[0] for x in sorted_combined]
    return sorted_a

a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]

print(sort_by_indexes(a, b))

print(sort_by_indexes(a, b, True))

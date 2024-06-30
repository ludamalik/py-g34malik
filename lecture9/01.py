
def sort_dict_by_key(d, reverse=False):
    sorted_items = sorted(d.items(), reverse=reverse)
    return dict(sorted_items)

d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
print(sort_dict_by_key(d))

print(sort_dict_by_key(d, True))

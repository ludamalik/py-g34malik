def average(*args):
    if len(args) == 0:
        raise ValueError("At least one number must be provided")
    return sum(args) / len(args)

print(average(*[1, 2, 3]))
print(average(1, 2, 3))

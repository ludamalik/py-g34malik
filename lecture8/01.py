def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib_list = []

for n in fib():
    if n > 610:
        break
    fib_list.append(n)

print(fib_list)

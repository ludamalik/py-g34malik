with open('sales.txt', 'r') as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    if 'laptop' in line:
        print(f"Рядок {index + 1}: {line.strip()}")

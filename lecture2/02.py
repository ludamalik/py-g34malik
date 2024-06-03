string=input("Введіть: ")
def sym(string):
#Ця функція перевіряє рядок на симетрію
    str_length = len(string)
    if str_length % 2 == 0:
        half_str = str_length // 2
        fh = string[:half_str]
        sh = string[half_str:]
        if fh == sh:
            return True
    return False
if sym(string):
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")
print()
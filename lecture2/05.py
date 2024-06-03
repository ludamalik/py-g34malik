from decimal import *
P = Decimal(input("Визначте основну суму: "))
r = Decimal(input("Визначте річну відсоткову ставку: "))
n = int(input("Визначте кількість разів нарахування відсотків на рік: "))
t = int(input("Визначте кількість років, за які нараховуються відсотки: "))
def complex_interest(P, r, n, t):
#Функція обчислює складні відсотки за заданою формулою A = P * (1 + (r / n)) ** (n * t)"""
    dec = r / Decimal(100)
    A = P * (1 + (dec / n)) ** (n * t)
    return A
getcontext().prec = 10
result = complex_interest(P, r, n, t)
print("Складні відсотки:", result)
print()
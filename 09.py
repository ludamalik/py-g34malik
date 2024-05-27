#Завдання 9

fv=int(input("Enter the desired future value: "))
air=float(input("Enter the annual interest rate: "))
noy=int(input("Enter the number of years the money will grow: "))
p=fv/(1+air)**noy
print("You will need to deposit this amount:", round(p, 2))

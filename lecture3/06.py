import random

rand_inp=random.randint(1, 100)

print ("*"*35)
print ("ГРА ПОЧАЛАСЬ")
print ("*"*35)

while True:
    user_inp=int(input ("Введіть ціле число в діапазоін від 1 до 100, [0 - вихід] "))
    if user_inp==0:
        print ("*"*35)
        print ("ГРА ЗАКІНЧИЛАСЬ ")
        break
    elif user_inp==rand_inp:
        print (f"Ваше число {user_inp}, число рулетки {rand_inp} - ви ВИГРАЛИ !!!")
        break
    elif user_inp>rand_inp:
        print ("Ваше число завелике !")
    else:
        print ("Ваше число замале !")
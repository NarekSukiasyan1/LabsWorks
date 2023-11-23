import random
print("Введите кол-во камней для игры от 4 до 30")
a = int(input())
if (a < 4 & a > 30):
    print("Неверное кол-во камней")
    exit()
while (True):
    print("Осталось ", a, "камней")
    print("Сколько камней от 1 до 3 хотите убрать")
    b = int(input())
    if (b != 1 | b != 2 | b != 3):
        print("Недопустимое число, попробуйте снова")
        continue
    a -= b
    print("Осталось ", a, "камней")
    if (a == 1):
        print("Вы победили")
        break
    c = random.randint(1, 3)
    if (c >= a):
        c -= 1
        if (c >= a):
            c -= 1
    a -= c
    if (a == 1):
        print("Вы проиграли")
        break

import math
try:
    angle = input("Введите угл в градусах")
    radians = (math.pi * float(angle)) / 180
    print(math.sin(radians))
    print(math.cos(radians))
    print(math.tan(radians))
except:
    print("Некоректный ввод числа")
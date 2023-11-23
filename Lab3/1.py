import math
angle = input("Введите угл в градусах")
try:
    radians = (math.pi * float(angle)) / 180
except:
    print("Некоректный ввод числа")
print(math.sin(radians))
print(math.cos(radians))
print(math.tan(radians))
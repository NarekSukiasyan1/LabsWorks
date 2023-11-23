import string
import re
i1 = 0
i2 = 0
print("Введите 1 вектор двумя числами через пробел")
try:
    i1 = int(input())
except:
    print("Erorr")
    exit()
try:
    i2 = int(input())
except:
    print("Erorr")
    exit()
a = [i1 // 10, i2 % 10]
print("Введите 2 вектор двумя числами через пробел")
try:
    i1 = int(input())
except:
    print("Erorr")
    exit()
try:
    i2 = int(input())
except:
    print("Erorr")
    exit()
b = [i1 // 10, i2 % 10]

print(a[0] * b[0] + a[1] * b[1])

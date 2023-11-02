import string 
import re
print("Введите 1 вктор двумя числами через пробел")
str =input()
str = re.sub(r"\s",'',str)
if str.isdigit():
    a = [int(str)//10, int(str)%10]
print("Введите 2 вtктор двумя числами через пробел")
str = input()
str = re.sub(r"\s",'',str)
if str.isdigit():
    b = [int(str)//10, int(str)%10]

print(a[0]*b[0]+a[1]*b[1])
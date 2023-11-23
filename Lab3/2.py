import math

def GCD(num1, num2): 
    if num1 > num2:
        max = num2 
    else: 
        max = num1 
    for i in range(1, max + 1): 
        if(( num1 % i == 0) and(num2 % i == 0 )): 
            gcd = i 
    return gcd 

num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))
try:
    print("GCD:", GCD(num1, num2))
    print("Math.gcd:", math.gcd(num1, num2))
except:
    print("Некоректный ввод")
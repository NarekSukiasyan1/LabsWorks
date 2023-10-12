a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c1 = 0
c2 = 0
for i in range(3):
    c1 += a % 10
    a = a // 10
    c2 += b % 10
    b = b // 10
if (c1 == c2):
    print("Счастливый билет")

else:
    print("Несчастный билет")

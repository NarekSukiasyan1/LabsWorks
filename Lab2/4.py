a = int(input("Введите число"))
res = 1
if (a < 0):
    print("ERor")
    exit
elif (a == 1 | a == 0):
    print("1")
    exit
for i in range(a):
    res *= i+1
print(res)

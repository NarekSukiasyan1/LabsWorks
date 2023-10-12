
print("Введите стороны треугольника построчно")

a = int(input())
b = int(input())
c = int(input())

isPossible = True

if(a > (b + c)):
    isPossible = False
elif(b > (a + c)):
    isPossible = False
elif(c > (a + b)):
    isPossible = False


if(isPossible):
    triangle = [a, b, c]
    triangle.sort
    a = triangle[0] ** 2
    b = triangle[1] ** 2 + triangle[2] ** 2
    if(a == b):
        print("Треугольник Прямоугольный")
    elif(a > b):
        print("Треугольник Тупоугольный")
    else:
        print("Треугольник остроугольный")
else:
    print("Это не тругольник")
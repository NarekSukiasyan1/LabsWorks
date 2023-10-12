from datetime import datetime
print("Вводите данные СТРОГО в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС")
try:
    t1 =datetime.fromisoformat(str(input("Введи время отправления:")))
    t2 =datetime.fromisoformat(str(input("Введи время прибытия:")))
    if t2 > t1:
        print("Поезд будет в пути :", t2 - t1)
    else:
        print("Время прибытия раньше отправления")
except:
    print("Некорректно введено время")
from datetime import timedelta
from datetime import date
print("Вводите данные СТРОГО в формате ГГГГ-ММ-ДД")
try:
    bithsday = date.fromisoformat(str(input("Введи дату своего дня рождения:")))
    days = bithsday + timedelta(days = 10000)
    print("10000 дней вам исполнится в :", days)
    #print("10000 дней вам исполнится в :", d_conv_time.day) для того чтобы вывести только день
    minuts = bithsday + timedelta(minutes = 1000000)
    print("1000000 минут вам исполнится в :", minuts)
    seconds = bithsday + timedelta(seconds = 1000000000)
    print("1000000000 секунд вам исполнится в :", seconds)
except:
    print("Некорректно введена дата")
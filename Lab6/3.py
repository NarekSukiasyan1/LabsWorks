mas = []
print("Введите массив, чтобы завершить ввод введите \'z\'")
while(True):
    a = input()
    try:
        a  = int(a)
    except:
        if(a =="z"):
            break
        else:
            print("Введено не число")
            exit()
    mas.append(a)
count = 0
maxcount = 0
maxcountindex = 0
for i in range(len(mas)):
    for j in range(i,len(mas)):
        if(mas[i]==mas[j]):
            count+=1
    if(count>maxcount):
        maxcount = count
        maxcountindex = i
        count = 0
    elif(count == maxcount):
        print("Моды не имеется")
        exit()
    else:
        count = 0
print("Мода массива:",mas[maxcountindex])
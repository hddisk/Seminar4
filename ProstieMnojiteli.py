def Mnojiteli(number):
    list = []
    for i in range(1, number):
        if number % i ==0:
            list.append(i)
    return list

num=int(input("Введите число "))
print(Mnojiteli(num))
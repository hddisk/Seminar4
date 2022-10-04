def Writing(k):
    list = [0]*(k+1)
    for i in range(0,k+1):
        list[i] = randint(0, 100)
    my_file = open("some.txt", "w")
    for i in range(k,1,-1):
        my_file.write(str(list[i])+"x^"+str(i)+"+")
    my_file.write(str(list[1])+"x+"+str(list[0])+"=0")
    my_file.close()
    
    
from random import randint
k=int(input("Введите число "))
Writing(k)
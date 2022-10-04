def Nepovtor(nmbrs):
    for i in range(10):
        index = 0
        for j in range(10):
            if nmbrs[i] == nmbrs[j] and i != j:
                index = 1
        if index ==0:
            print(nmbrs[i])

from random import randint
numbers = [0]*10
for i in range(10):
    numbers[i] = randint(0, 10)
print(numbers)
Nepovtor(numbers)
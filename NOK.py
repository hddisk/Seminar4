def NaOK(number1, number2):
    return(number1*number2/NaOD(number1, number2))
        
def NaOD(number1, number2):
    list = []
    for i in range(2, number1):
        for j in range(2, number2):
            if number1 % i ==0 and number2 % j ==0 and i==j:
                list.append(i)
    return list[-1]

num1=int(input("Введите первое число "))
num2=int(input("Введите второе число "))
print(NaOK(num1, num2))
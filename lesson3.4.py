#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
num3 = int(input("Введите третье число"))
sum = ((num1 > 0) + (num2 > 0) + (num3 > 0))
if sum==0:
    print('Все числа отрицательные')
elif sum==1:
    print('Два отрицательных, одно положительное')
elif sum==2:
    print('Два положиткльных,одно отрицательное')
elif sum==3:
    print('Все числа положительные')


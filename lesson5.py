


#1. tode Вводится с клавиатуры десятичная дровь (пример "10/3") необходимо вычислить значение данной дроби (3.333)
text = input('введите с клавиатуры десятичную дровь (пример 10/3)')
number1 = str(text.find(0,3))
number2 = str(text.rfind(-1,-1))
print(number1+number2)

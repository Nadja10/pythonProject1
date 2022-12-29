#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
text = input('Введите предложение')
text = text.replace(' ','-')
print(text)
#2
text = text.split()
text = '-'.join(text)
print(text)

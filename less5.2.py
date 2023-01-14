while True:
    s = input("Выберите математическое действие: '+', '-', '*', '/'")
    if s in ('+', '-', '*', '/'):
        x = int(input('Введите первое число'))
        y = int(input('Введите второе число'))
        if s == '+':
            sum = x + y
            print(sum)
        elif s == '-':
            subtrac = x - y
            print(subtrac)
        elif s == '*':
            multipl = x*y
            print(multipl)
        elif s == '/':
            if y != 0:
                divis = x/y
                print(divis)
            else:
                print('на ноль делить нельзя! ')




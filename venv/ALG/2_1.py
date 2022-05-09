# Калькулятор
sign = None
n1 = None
n2 = None
while sign != '0':
    n1 = float(input('Введите первое число: '))
    sign = input('Введите знак операции (+, -, *, /): ')
    n2 = float(input('Введите второе число: '))
    if n2 == 0:
        print('На ноль делить нельзя!')
    else:
        if sign == '+':
            print(n1+n2)
        elif sign == '-':
            print(n1-n2)
        elif sign == '*':
            print(n1*n2)
        elif sign == '/':
            print(n1/n2)
        elif sign == '0':
            print('Вы вышли из калькулятора')
        else:
            print('Введен неверный знак операции!')
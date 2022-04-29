a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if b < a < c or c < a < b:
    print(f'Среднее: {a}')
elif a < b < c or c < b < a:
    print(f'Среднее: {b}')
else:
    print(f'Среднее:{c}')
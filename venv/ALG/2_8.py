
num_count = int(input('Введите количество вводимых чисел: '))
digit = int(input('Введите искомую цифру: '))
flag = 0
for i in range(num_count):
    num = int(input(f'Введите число № {i+1}: '))
    while num != 0:
        if num % 10  == digit:
            flag += 1
        num = num // 10
print(f'Цифра {digit} в указанной последовательности повторилась {flag} раз.')
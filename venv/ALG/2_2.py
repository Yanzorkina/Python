# Посчитать сколько цифр в числе четных, сколько нечетных
num = int(input('Введите натуральное число: '))
save_num = num
even_nums = 0
odd_nums = 0
while num != 0:
    if (num % 10) % 2 == 0:
        even_nums += 1
    else:
        odd_nums += 1
    num = num // 10
print(f'В числе {save_num} присутствует {even_nums} четных и {odd_nums} нечетных цифр.')
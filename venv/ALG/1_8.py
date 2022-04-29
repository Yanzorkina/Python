user_year = int(input('Введите год: '))
if (user_year % 4) == 0:
    print(f'Год {user_year} - Високосный')
else:
    print(f'Год {user_year} - Невисокосный')
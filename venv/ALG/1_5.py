import string
a = input('Введите первую букву (используйте нижний регистр): ')
b = input('Введите вторую букву (используйте нижний регистр): ')
a_number = string.ascii_lowercase.find(a) + 1
b_number = string.ascii_lowercase.find(b) + 1
l_dif = b_number - a_number - 1
print(f'Буква {a} в алфавите по счету на позиции {a_number},'
      f'\nбуква {b} - на позиции {b_number},\nмежду ними {l_dif} букв.')
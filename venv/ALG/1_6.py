import string

a = int(input('Введите номер буквы из алфавита: '))
print(f'Ваша буква: {string.ascii_lowercase[a-1]}')
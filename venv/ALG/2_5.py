# Таблица символов ASCII
n = 32
str_view = ''
while n < 128:
    for i in range(10):
        if n < 128:
            str_view = str_view + (f'{n} - {chr(n)}'.center(10))
            n = n+1
    print(f'{str_view} \n')
    str_view = ''
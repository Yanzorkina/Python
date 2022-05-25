# 5_2
# A2 и C4F
#Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import defaultdict
def get_ten(key_dict, str_sixteen): # Возвращает int из строки с шестнадцатиричным числом
    number = 0
    n = 0
    str_sixteen = str_sixteen[::-1]
    for i in str_sixteen:
        number += key_dict[i][0] * 16**n
        n += 1
    return number
def get_sixteen(key_dict, number_ten): # Возвращает список с шестнадцатиричным числом из int
    str_sixteen = []
    while number_ten != 0:
        str_sixteen.append(key_dict[number_ten % 16][0])
        number_ten = number_ten // 16
    return(str_sixteen[::-1])
sixteen_signs = '0123456789ABCDEF'
key_sixteen = defaultdict(list)
key_ten = defaultdict(list)
for k in range(len(sixteen_signs)):
    key_sixteen[sixteen_signs[k]].append(k)
    key_ten[k].append(sixteen_signs[k])
f_number = (input('Введите первое число: '))
s_number = (input('Введите второе число: '))
fn_ten = get_ten(key_sixteen, f_number)
sn_ten = get_ten(key_sixteen, s_number)
print(f'В десятичном счислении эти числа: {fn_ten}, {sn_ten}')
sum_ten = fn_ten + sn_ten
multy_ten = fn_ten * sn_ten
str_sum_sixteen = get_sixteen(key_ten, sum_ten)
str_multy_sixteen = get_sixteen(key_ten, multy_ten)
print(f'Сумма чисел: {str_sum_sixteen}')
print(f'Произведение чисел: {str_multy_sixteen}')
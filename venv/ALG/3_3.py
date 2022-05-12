# 3_3
from random import random
len_list = int(input("Введите количество элементов списка: "))
first_list = []
min_num = 100
min_index = 0
max_num = 0
max_index = 0
for i in range(len_list):
    first_list.append(int(random()*100))
print(f'Список сгенерирован: {first_list}')
for n in range(len(first_list)):
    if first_list[n] < min_num:
        min_num = first_list[n]
        min_index = n
    if first_list[n] > max_num:
        max_num = first_list[n]
        max_index = n
print(f'Мин значение: {min_num} на позиции {min_index}\nМакс значание: {max_num} на позиции {max_index}')
first_list[min_index] = max_num
first_list[max_index] = min_num
print(f'Редактируем список: {first_list}')
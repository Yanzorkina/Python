# 3_2
from random import random
len_list = int(input("Введите количество элементов списка: "))
first_list = []
second_list = []
for i in range(len_list):
    first_list.append(int(random()*100))
print(f'Список сгенерирован: {first_list}')
for n in range(len(first_list)):
    if first_list[n] % 2 == 0:
        second_list.append(n)
print(second_list)
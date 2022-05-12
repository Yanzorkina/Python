# 3_6
from random import random
len_list = int(input("Введите количество элементов списка: "))
main_list = []
for i in range(len_list):
    main_list.append(int(random()*100))
print(f'Список сгенерирован: {main_list}')
max_ind = main_list.index(max(main_list))
min_ind = main_list.index(min(main_list))
print('Индексы максимального и минимального чисел: ',max_ind, ' и ', min_ind)
if max_ind < min_ind:
    mid_sum = sum(main_list[(max_ind+1):(min_ind)])
else:
    mid_sum = sum(main_list[(min_ind+1):(max_ind)])
print(f'Результат: {mid_sum}')
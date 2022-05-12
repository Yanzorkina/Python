# 3_5
from random import random
len_list = int(input("Введите количество элементов списка: "))
main_list = []
m_m_index = 0
for i in range(len_list):
    main_list.append(int(random()*100) - 50)
print(f'Список сгенерирован: {main_list}')
max_min_num = min(main_list)
for n in range(len(main_list)):
    if main_list[n] < 0:
        if main_list[n] > max_min_num:
            max_min_num = main_list[n]
            m_m_index = n
print(f'Самым большим отрицательным числом является {max_min_num}, на позиции {m_m_index}')
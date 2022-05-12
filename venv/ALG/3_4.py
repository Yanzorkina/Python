# 3_4
from random import random
len_list = int(input("Введите количество элементов списка: "))
main_list = []
count = {}
for i in range(len_list):
    main_list.append(int(random()*10))
print(f'Список сгенерирован: {main_list}')
for n in range(len(main_list)):
    if count.get(main_list[n]) == None:
        count.update({main_list[n]:1})
    else:
        count[main_list[n]] += 1
print(count)
print(f'Чаще остальных повторяется число : {max(count, key=count.get)}')
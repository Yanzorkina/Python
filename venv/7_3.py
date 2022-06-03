# 7_3 Массив размером 2m+1. Найти медиану. Временная сложность О(n**2), пространственная O(n)
# В цикле m раз удалим максимальное и минимальное значение.

from random import randint

m = int(input('Для создания массива размером 2m+1, введите m: '))
num_list = []

for i in range(2*m+1):
    num_list.append(randint(1, 100))
print('Массив сгенерирован: ', num_list)

for j in range(m):
    num_list.remove(max(num_list))
    num_list.remove(min(num_list))
print(f'Медиана в созданном массиве: {num_list[0]}')
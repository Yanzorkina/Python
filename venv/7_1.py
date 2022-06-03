'''
7_1
Доработаем алгоритм таким образом, чтобы "пузырки" не тащили отрицательные через весь массив,
а сразу перетащим все отрицательные числа в правую часть. Это увеличит пространчтвенную сложность
на n, чтобы оставить возможность итерировать список, объявим это сразу.
Закомментированные вызовы print - вспомогательные.
Временная сложность О(n**2)
Пространственная O(n)
'''

from random import randint
def bubble_sort(numbers):
    ind = len(numbers)
    static_len = len(numbers)
    numbers.extend('X' * len(numbers))
    # print(*numbers, ' - расширенный список, фиксирующий максимально занимаемую память')
    for k in range(static_len):
        if numbers[k] != 'X':
            if numbers[k] < 0:
                numbers[ind], numbers[k] = numbers[k], numbers[ind]
                ind += 1
    # print(*numbers, ' - отрицательные числа смещены на "вакантные" позиции')
    for l in range(static_len):
        numbers.remove('X')
    # print(*numbers, " - результат первоначальной оптимизации")
    swapped = False
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(i):
            if numbers[j] < numbers[j + 1]:
                numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return numbers
num_list = []
for i in range(10):
    num_list.append(randint(-100, 99))
print(*num_list, ' - несортированный массив')
print(*bubble_sort(num_list), ' - результат сортировки')
# 7_2 Сортировка слиянием одномерного массива вещественных чисел от 0 до 50.
# Временная сложность О(log(n)), пространственная О(n**2) из-за рекурсивности.


from random import triangular


def merge_sort(num_list):
    if len(num_list) > 1:
        mid = len(num_list) // 2
        left = num_list[:mid]
        right = num_list[mid:]
        # рекурсивно вызываем функцию для левой и правой частей
        merge_sort(left)
        merge_sort(right)
        # отдельные счетчики для левой, правой частей и общий
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                num_list[k] = left[i]
                i += 1
            else:
                num_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            num_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            num_list[k] = right[j]
            j += 1
            k += 1

my_num_list = []
for l in range(10):
    my_num_list.append(round((triangular(0, 50)), 3))
    
print(my_num_list)
merge_sort(my_num_list)
print(my_num_list)
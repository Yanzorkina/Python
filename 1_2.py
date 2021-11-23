#Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
#Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#* Решить задачу под пунктом b, не создавая новый список.


number = 1
cube_numbers = []
num_sum = 0
all_sum = 0
sums = []
all_sum17 = 0

for i in range(1, 1001):
    if number % 2 != 0:
        cube_numbers.append(number**3)
    number += 1
print(cube_numbers)

copy_num = cube_numbers.copy()
copy_num17 = cube_numbers.copy()

for n in range(len(cube_numbers)):
    num_sum = 0
    while cube_numbers[n] > 0:
        digit = cube_numbers[n] % 10
        num_sum = num_sum + digit
        cube_numbers[n] = cube_numbers[n] // 10

    if num_sum % 7 == 0:
        all_sum = all_sum + copy_num[n]
        sums.append(copy_num[n])


print(sums)
print(all_sum)


for k in range(len(copy_num17)):
    num_sum = 0
    copy_num17[k] += 17
    while copy_num17[k] > 0:
        digit = copy_num17[k] % 10
        num_sum = num_sum + digit
        copy_num17[k] = copy_num17[k] // 10

    if num_sum % 7 == 0:
        all_sum17 = all_sum17 + (copy_num[k] + 17)

print(all_sum17)













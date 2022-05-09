# Отзеркалим число
# Решение через STR:
# nums = input('Введите число: ')
# rev_num = ''
# for num in nums:
#     rev_num = rev_num + nums[-1]
#     nums = nums[0:-1]
# print(f'Отзеркаленное число: {rev_num}')
# Математическое решение:
nums = int(input('Введите число: '))
rev_num = 0
while nums != 0:
    rev_num = (rev_num * 10) + (nums % 10)
    nums = nums // 10
print(f'Отзеркаленное число: {rev_num}')
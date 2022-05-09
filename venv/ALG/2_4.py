# Сумма элементов ряда
n = int(input('Введите количество элементов ряда: '))
step = 1
sum = 0
for i in range(n):
    sum = sum + step
    step = step*(-0.5)
print(sum)
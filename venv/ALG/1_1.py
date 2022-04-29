n = int(input('Введите трехзначное число: '))

a = n // 100
b = (n % 100) // 10
c = n % 10
sum = a + b + c
prod = a * b * c

print(f"Сумма чисел равна {sum}")
print(f"Произведение чисел равно {prod}")

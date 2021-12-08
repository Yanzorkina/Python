
nums_gen = (print(num) for num in range(1, (int(input("Введите число n: ")) + 1)) if num % 2 != 0)

print(type(nums_gen))
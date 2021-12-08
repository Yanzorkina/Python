

def num_gen(num):
    for i in range(1, num+1):
        if i % 2 != 0:
            yield i


for n in num_gen(int(input("Это генератор нечетных чисел от 1 до n. Введите число n: "))):
    print(n)
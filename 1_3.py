#Реализовать склонение слова «процент» во фразе «N процентов».
#Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:



pc = []
for i in range(101):
    pc.append(i)

for i, val in enumerate(pc):

    if val % 10 == 1 and val != 11:
        print(i, 'процент', end="\n")

    elif val % 10 >= 2 and val % 10 <= 4 and not (12 <= val <= 14):
        print(i, "процента")
    else:
        print(i, "процентов", end="\n")



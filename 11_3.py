class NumbersOnlyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []

print("Это программа добавления чисел в список. Чтобы выйти и получить список, введи 'Q'")

while True:
    try:
        inp_data = input("Введите число: ")
        if inp_data == "Q":
            print(num_list)
            break
        if not inp_data.replace(".", "").isdigit():
            raise NumbersOnlyErr("Вы ввели не число!")

    except NumbersOnlyErr as err:
        print(err)
    else:
        num_list.append(float(inp_data))

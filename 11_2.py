class DontUseZeroErr(Exception):
    def __init__(self, txt):
        self.txt = txt


a_num = input("Введите делимое: ")
b_num = input("Введите делитель: ")

try:
    a_num = float(a_num)
    b_num = float(b_num)
    if b_num == 0:
        raise DontUseZeroErr("Нельзя делить на ноль!")
except ValueError:
    print("Вы ввели не число")
except DontUseZeroErr as err:
    print(err)
else:
    print(f"Частное равняется: {round(a_num / b_num, 3)}")



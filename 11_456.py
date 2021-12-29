class OfficeStuffWarehouse:
    allocation = {"main_warehouse": [0, 0, 0],
                  "sales_dept": [0, 0, 0],
                  "bookkeeping": [0, 0, 0],
                  "reception": [0, 0, 0]
                  }

    items = {"Всего единиц оборудования": 0,
             "Всего принтеров": 0,
             "Всего сканеров": 0,
             "Всего ксероксов": 0
             }


class OfficeEquipment:

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
        self.id = None
        OfficeStuffWarehouse.items["Всего единиц оборудования"] += 1

    def move(self, destination, departure="shop"):

        try:
            self.destination = destination
            self.departure = departure
            if departure == "shop":
                OfficeStuffWarehouse.allocation[destination][self.id] += 1

            elif OfficeStuffWarehouse.allocation[departure][self.id] > 0:
                OfficeStuffWarehouse.allocation[departure][self.id] -= 1
                OfficeStuffWarehouse.allocation[destination][self.id] += 1

            else:
                print("В месте отправки нет перемещаемого предмета")
        except:
            print("Ошибка перемещения! Такого отдела не существует!")


class Printer(OfficeEquipment):

    def __init__(self, color, weight, bnw_print):
        super().__init__(color, weight)
        self.bnw_print = bnw_print
        self.id = 0
        OfficeStuffWarehouse.items["Всего принтеров"] += 1


class Scanner(OfficeEquipment):
    def __init__(self, color, weight, scan_resoluton):
        super().__init__(color, weight)
        self.scr_resolution = scan_resoluton
        self.id = 1
        OfficeStuffWarehouse.items["Всего сканеров"] += 1


class Xerox(OfficeEquipment):
    def __init__(self, color, weight, speed):
        super().__init__(color, weight)
        self.speed = speed
        self.id = 2
        OfficeStuffWarehouse.items["Всего ксероксов"] += 1


p1 = Printer("gray", 12, True)
s1 = Scanner("white", 9, "4K")
x1 = Xerox("black", 20, 100)
x2 = Xerox("blue", 15, 50)

print("Покупаем принтер и помещаем на главный склад")
p1.move("main_warehouse")
print(OfficeStuffWarehouse.allocation)
print()
print("Переносим принтер с главного склада в бухгалтерию")
p1.move("bookkeeping", "main_warehouse")
print(OfficeStuffWarehouse.allocation)
print()
print("Покупаем сканнер, следующим шагом отнесем его в отдел продаж")
s1.move("main_warehouse")
print(OfficeStuffWarehouse.allocation)
s1.move("sales_dept", "main_warehouse")
print(OfficeStuffWarehouse.allocation)
print()
print("Покупаем ксерокс и мимо склада несем на ресепшен, а потом еще один")
x1.move("reception")
print(OfficeStuffWarehouse.allocation)
x2.move("reception")
print(OfficeStuffWarehouse.allocation)
print()
print("Запросим принтер из отдела, где его нет")
p1.move("reception", "sales_dept")
print(OfficeStuffWarehouse.items)
print()
print("Пробуем ввести некорректные данные при перемещении")
p1.move("home", "bookkeeping")
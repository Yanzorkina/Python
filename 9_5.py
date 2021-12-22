class Stationery:
    def __init__(self,  title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
       print(f'Запуск отрисовки ручкой {self.title}')

class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')

#######################################################################################################
p_1 = Pen("red")
p_1.draw()
p_2= Pencil("white")
p_2.draw()
p_3 = Handle("black")
p_3.draw()





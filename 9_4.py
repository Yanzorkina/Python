class Car:
    def __init__(self,  s, c, n, p=False):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        self.direction = direction
        return f'Машина повернула {self.direction}'

    def show_speed(self):
        return f'Машина {self.name} едет со скоростью {self.speed} км/ч'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f"{self.name}: превышение допустимой скорости на {self.speed - 60} км/ч"
        else:
            super().show_speed()

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f"{self.name}: превышение допустимой скорости {self.speed - 40} км/ч"
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n, p=True)

class SportCar(Car):
    pass



#######################################################################################################
lada = TownCar(120, "red", "Lada-2110")

mazda = WorkCar(45, "red", "Mazda 3")

golf = PoliceCar(96, "white", "W-golf")


cars = [lada, mazda, golf]

for car in cars:
    print(car.go())
    print(car.stop())
    print(car.turn("направо"))
    print(car.show_speed())





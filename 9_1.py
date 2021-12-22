from time import sleep

class TrafficLight:

    __color = 'красный'

    # методы класса
    def running(self):
        while True:
            print('red')
            sleep(7)
            print('yellow')
            sleep(2)
            print('green')
            sleep(7)
            print('yellow')
            sleep(2)

a = TrafficLight()
a.running()




class Road:


    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, w=25, t=5):
        return f'{int((self._length * self._width * w * t) / 1000)} т'


r = Road(5000, 6.52)
print(r.mass())



from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    def __str__(self):
        return f"{self.consuption}"

    def __add__(self, other):
        return Sum(self.consuption + other.consuption)

    @property
    @abstractmethod
    def consuption(self):
        pass


class Coat(Clothes):
    @property
    def consuption(self):
        return (self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consuption(self):
        return (self.param * 2) + 0.3


""" Делаем отдельный дочерний класс для суммирования. Он возвращает то же самое, что и принимает """


class Sum(Clothes):
    @property
    def consuption(self):
        return self.param


thing_1 = Costume(1.7)
thing_2 = Coat(40)

print(thing_1)
print(thing_2)
print(thing_1 + thing_2 + thing_1)

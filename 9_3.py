class Worker:
    def __init__(self,  name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'

woman = Position("Алина", "Янзоркина", "PR", 6000, 550)
print(woman.get_full_name())
print(woman.get_total_income())
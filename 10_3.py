class Cell:

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"{'@' * (int(self.number))}"

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            return Cell(self.number - other.number)
        else:
            return "Операция невозможна"

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, row_lenght):
        return '\n'.join(['@' * row_lenght for i in range(self.number // row_lenght)]) \
               + '\n' + '@' * (self.number % row_lenght)


first_cell = Cell(8)
print(first_cell)
second_cell = Cell(6)
print(first_cell + second_cell)

print(first_cell.make_order(3))
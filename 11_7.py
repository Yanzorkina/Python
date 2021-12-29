class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"({self.a} + {self.b}i)"

    def __add__(self, other):
        return ComplexNumber((self.a + other.a), (self.b + other.b))

    def __mul__(self, other):
        return ComplexNumber(((self.a * other.a) - (self.b * other.b)), ((self.b * other.a) + (self.a * other.b)))


g = ComplexNumber(3, 5)
print(g)

h = ComplexNumber(4, -5)
print(h)

print(g + h)
print(g * h)




class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):

        show_it = "".join(str(self.matrix)).lstrip("[[").replace("], [", "\n").rstrip("]]").replace(", ", "   ")
        return f"{show_it} \n"

    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range
        (len(self.matrix[0]))] for i in range(len(self.matrix))])


m_1 = Matrix([[4, 5], [6, 7], [8, 9]])
print(m_1)

m_2 = Matrix([[6, 2], [5, 1], [6, 3]])
print((m_2))

print(m_1 + m_2)
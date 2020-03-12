class Matrix:
    def __init__(self, data):
        self.data = data
        self.matrix = data

    def __add__(self, other):
        result = None
        string = len(self.data)
        column = len(other.data[0])
        for i in range(string):
            for j in range(column):
                self.data[i][j] = self.data[i][j] + other.data[i][j]
            result = self.data
        return Matrix(result)

    def __str__(self):
        self.matrix = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.data])
        return str(self.matrix)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(f'Матрица №1\n{matrix_1}')
print(f'Матрица №2\n{matrix_2}')
print(f'Сумма матриц:\n{matrix_1 + matrix_2}')

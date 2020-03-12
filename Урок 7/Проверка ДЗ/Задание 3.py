class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        if self.cells >= other.cells:
            return self.cells - other.cells
        else:
            return 'Отрицательный результат.'

    def __mul__(self, other):
        return self.cells * other.cells

    def __truediv__(self, other):
        return self.cells // other.cells

    def make_order(self, order):
        line = [['*' for i in range(order)] for i in range(self.cells // order)]
        line.append(['*' for i in range(self.cells - (order * (self.cells // order)))])
        structure = '\n'.join([''.join([str(j) for j in i]) for i in line])
        print(len(structure))
        return structure


cell_1 = Cell(20)
cell_2 = Cell(10)
print(f'Сложение!\nРезультат (кол-во ячеек) - {cell_1 + cell_2}\n')
print(f'Вычитание!\nРезультат (кол-во ячеек) - {cell_1 - cell_2}\n')
print(f'Умножение!\nРезультат (кол-во ячеек) - {cell_1 * cell_2}\n')
print(f'Деление!\nРезультат (кол-во ячеек) - {cell_1 / cell_2}\n')
print(f'Структура клекти:\n{cell_1.make_order(3)}')

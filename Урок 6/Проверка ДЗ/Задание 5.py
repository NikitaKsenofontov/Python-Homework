class Stationery:
    def __init__(self, title):
        self.stationery_title = title

    def draw(self):
        print(f'Запуск отрисоки по умолчанию')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисоки {self.stationery_title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисоки {self.stationery_title}')


default_process = Stationery(None)
default_process.draw()
process1 = Pen('ручкой')
process1.draw()
process2 = Pencil('карандашом')
process2.draw()

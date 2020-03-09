from random import randint

side = ['лево', 'право']


class Car:
    def __init__(self, speed, color, name, is_police):
        self.car_speed = speed
        self.car_color = color
        self.car_name = name
        self.car_is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на{side[direction]}') if direction == 1 else print(f'Машина повернула на{side[direction]}')

    def show_speed(self):
        print(f'Скорость автомобиля - {self.car_speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.car_speed > 60:
            print(f'Превышение скорости на {self.car_speed - 60}км/ч')
        print(f'Скорость автомобиля - {self.car_speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.car_speed > 60:
            print(f'Превышение скорости на {self.car_speed - 60}км/ч')
        print(f'Скорость автомобиля - {self.car_speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(80, 'Красная', 'Городская машина', False)
print(f'Тип - {car1.car_name}, Цвет - {car1.car_color }, Скорость - {car1.car_speed}км/ч, Полиция - {car1.car_is_police}')
print('Совершенные действия')
car1.go()
car1.turn(randint(0, 1))
car1.show_speed()
car1.stop()
print('-' * 50)
car2 = SportCar(200, 'Желтая', 'Спортивная машина', False)
print(f'Тип - {car2.car_name}, Цвет - {car2.car_color }, Скорость - {car2.car_speed}км/ч, Полиция - {car2.car_is_police}')
print('Совершенные действия')
car2.go()
car2.turn(randint(0, 1))
car2.show_speed()
car2.stop()
print('-' * 50)
car3 = WorkCar(30, 'Черная', 'Рабочая машина', False)
print(f'Тип - {car3.car_name}, Цвет - {car3.car_color }, Скорость - {car3.car_speed}км/ч, Полиция - {car3.car_is_police}')
print('Совершенные действия')
car3.go()
car3.turn(randint(0, 1))
car3.show_speed()
car3.stop()
print('-' * 50)
car4 = PoliceCar(60, 'Синяя', 'Полицейчкая машина', True)
print(f'Тип - {car4.car_name}, Цвет - {car4.car_color }, Скорость - {car4.car_speed}км/ч, Полиция - {car4.car_is_police}')
print('Совершенные действия')
car4.go()
car4.turn(randint(0, 1))
car4.show_speed()
car4.stop()

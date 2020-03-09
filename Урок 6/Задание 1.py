from time import sleep


class TrafficLight:
    __tl_color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        while True:
            print(f'\033[31m\033[1m {self._TrafficLight__tl_color[0]}')
            sleep(7)
            print(f'\033[33m\033[1m {self._TrafficLight__tl_color[1]}')
            sleep(2)
            print(f'\033[32m\033[1m {self._TrafficLight__tl_color[2]}')
            sleep(7)
            print(f'\033[33m\033[1m {self._TrafficLight__tl_color[1]}')
            sleep(2)


a = TrafficLight()
a.running()

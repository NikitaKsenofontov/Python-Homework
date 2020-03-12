from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.v = size

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, growth):
        self.h = growth

    @property
    def consumption(self):
        return 2 * self.h + 0.3


print(f'Нужно {Coat(6.5).consumption + Suit(3).consumption}м ткани')

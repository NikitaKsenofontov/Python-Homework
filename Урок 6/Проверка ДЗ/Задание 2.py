class Road:
    def __init__(self, road_length, road_width):
        self._road_length = road_length
        self._road_width = road_width

    def asphalt_mass(self):
        print(f'Для покрытия всего дорожного полотна необходимо'
              f'{(self._road_length * self._road_width * 25 * 5) / 1000: .0f}т асфальта.')


asphalt_mass_estimate = Road(20, 5000)
asphalt_mass_estimate.asphalt_mass()

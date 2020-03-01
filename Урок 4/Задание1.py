from sys import argv

path, output_per_hour, rate_per_hour, prize = argv

print(f'Заработная плата сотрудника - {int(output_per_hour) * int(rate_per_hour) + int(prize)}')

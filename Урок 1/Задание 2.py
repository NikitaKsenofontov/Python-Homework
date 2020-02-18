user_time = int(input("Пожалуйста укажите время в секундах: "))

while user_time < 0:
    user_time = int(input("Отрицательного времени не бывает: "))

hours = user_time // 3600
minutes = user_time // 60
seconds = user_time - minutes * 60

print('Время: %02d:%02d:%02d' % (hours, minutes, seconds))

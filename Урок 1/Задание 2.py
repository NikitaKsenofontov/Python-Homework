user_time = int(input("Пожалуйста укажите время в секундах: "))

hours = user_time // 3600
minutes = user_time // 60
seconds = user_time - minutes * 60

print('%02d:%02d:%02d' % (hours, minutes, seconds))

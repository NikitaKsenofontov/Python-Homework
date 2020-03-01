def user_data(name, surname, middle_name, birth_year, city, e_mail, mobile):
    print(f'ФИО: {surname} {name} {middle_name}\nГод рождения: {birth_year}\n'
          f'Город проживания: {city}\nE-mail: {e_mail}\nТелефон: {mobile}')


user_data(name='Никита', surname='Ксенофонтов', middle_name='Ильич', birth_year=1993, city='Москва',
          e_mail='mr.ksenofontov@mail.ru', mobile=89295054859)

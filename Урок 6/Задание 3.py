class Worker:
    def __init__(self, worker_name, worker_surname, worker_position, wage, bonus):
        self.worker_name = worker_name
        self.worker_surname = worker_surname
        self.worker_position = worker_position
        self._worker_income = {'Зарплата': wage, 'Премия': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'ФИ сотрудника: {self.worker_surname} {self.worker_name}')

    def get_total_income(self):
        print(f'Должность: {self.worker_position}\n'
              f'Доход: {self._worker_income["Зарплата"] + self._worker_income["Премия"]}')


data = Position('Никита', 'Ксенофонтов', 'Менеджер', 50000, 20000)
data.get_full_name()
data.get_total_income()

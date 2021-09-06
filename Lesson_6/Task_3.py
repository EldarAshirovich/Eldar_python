import pydoc

"""
Autor Sabri Eldar

    3. Реализовать базовый класс Worker (работник).
    определить атрибуты: name, surname, position (должность), income (доход);
    последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
    проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

class Worker:
    
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position, self._incom = name, surname, position, {"wage": wage, "bonus": bonus}
        
class Position(Worker):
    
    def get_full_name(self):
        result = f"{self.name} {self.surname}"
        return result
        
    def get_total_income(self):
        result = f'{self._incom["wage"] + self._incom["bonus"]}'
        return result

workers = Position("Ростислав", "Михаиленко", "Директор", 40000, 5000), Position("Дмитрий", "Бурунов", "Менеджер", 30000, 4000), Position("Алексей", "Иванов", "Слесарь", 20000, 3000)
i = 0
while i < len(workers):
    print('{:-^50}'.format('Работник №'+str(i+1)))
    print(f"Имя: {workers[i].name}")
    print(f"Фамилия: {workers[i].surname}")
    print(f"Должность: {workers[i].position}")
    print(f"Доход: {workers[i]._incom}")
    print(f"Полное имя: {workers[i].get_full_name()}")
    print(f"Доход с учётом премии: {workers[i].get_total_income()}\n")
    i+=1
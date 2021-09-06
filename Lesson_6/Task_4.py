import pydoc

"""
Autor Sabri Eldar

    4. Реализуйте базовый класс Car.
    у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police = 0):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police
    
    def go(self):
        print(f"Автомобиль марки: {self.name} начал движение!")
        
    def stop(self):
        print(f"Автомобиль марки: {self.name} остановился!")
        
    def turn(self, direction):
        print(f"Автомобиль марки: {self.name} повернул на {direction}!")
    
    def show_speed(self):
        print(f"Текущая скорость авто: {self.speed}")
        
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Превышен скоростной режим!")

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Превышен скоростной режим!")
    
class SportCar(Car):
    def show_speed(self):
        print(f"Спортивный автомобиль!")
    
class PoliceCar(Car):
    def show_speed(self):
        print(f"Полицейский автомобиль!")
    
cars = TownCar(80, 'Зелёный', 'Toyota'), TownCar(59, 'Красный', 'Daewoo'), WorkCar(60, 'Бежевый', 'Приора'), WorkCar(38, 'Серебристый', 'Honda'), SportCar(240, 'Чёрный', 'Мерседес'), PoliceCar(120, 'Белый', 'BMW', 1)
i=0
while i < len(cars):
    print('{:-^50}'.format('Автомобиль: '+cars[i].name))
    cars[i].go()
    cars[i].turn("лево")
    cars[i].stop()
    cars[i].show_speed()
    print()
    i+=1
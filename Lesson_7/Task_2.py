import pydoc
from abc import ABC, abstractmethod

"""
Autor Sabri Eldar

    2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
    К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
    Это могут быть обычные числа: V и H, соответственно. 
    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
    Проверить работу этих методов на реальных данных.
    Реализовать общий подсчет расхода ткани.
    Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

class Clothes(ABC):
    
    def __init__(self, style, size):
        self.style = style
        self.size = size
    
    @abstractmethod
    def fabric_calculation(self):
        pass


class Сoat(Clothes):
    @property
    def fabric_calculation(self):
        all_summ = 0
        summ_coat = f'Расход ткани для Пальто дизайн {self.style}:\n'
        for i, el in enumerate(self.size):
            summ_coat += f"Размер:{el} - Расход: {int(el) / 6.5 + 0.5:.2f} м.\n"
            all_summ += int(el) / 6.5 + 0.5
        summ_coat += f"Общий расход ткани в метрах {all_summ:.2f}\n"
        return summ_coat

class Сostume(Clothes):
    @property
    def fabric_calculation(self):
        all_summ = 0
        summ_coat = f'Расход ткани для Пальто дизайн {self.style}:\n'
        for i, el in enumerate(self.size):
            summ_coat += f"Размер:{el} - Расход: {2* int(el) + 0.3:.2f} м.\n"
            all_summ += 2 * int(el) + 0.3
        summ_coat += f"Общий расход ткани в метрах {all_summ:.2f}\n"
        return summ_coat

list_coats = [
    ['redingot', [42, 44, 46, 48, 50, 52]], 
    ['daflcot', [40, 42, 44, 46, 48, 50]], 
    ['reglan', [36, 38, 40, 42]], 
    ['trenchcot', [46, 48, 50, 52, 54]]
    ]

list_costume = [
    ['classic', [1.5, 1.6, 1.7, 1.8, 1.9]], 
    ['fitted', [1.4, 1.5, 1.6, 1.7, 1.8, 1.9]], 
    ['sport', [1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1]]
    ]

print('{:-^50}\n'.format("Пальто"))
i=0
while i < len(list_coats):
    print(Сoat(list_coats[i][0], list_coats[i][1]).fabric_calculation)
    i+=1
i=0
print('{:-^50}\n'.format("Костюмы"))
while i < len(list_costume):
    print(Сostume(list_costume[i][0], list_costume[i][1]).fabric_calculation)
    i+=1
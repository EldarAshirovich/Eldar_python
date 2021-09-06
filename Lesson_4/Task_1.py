import pydoc
from sys import argv

"""
Autor Sabri Eldar

    1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
    Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
    Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
def wagesFunc(pih, rph, pim):
    wages = pih * rph + pim
    return wages
prodInHours = float(argv[1]) # Выработка в часах
ratePerHours = float(argv[2]) # Ставка в час
premium = float(argv[3]) # Премия
wages = 0 # Заработная плата
wages = wagesFunc(prodInHours, ratePerHours, premium)
print(f"Результат заработной платы составил: {wages}")

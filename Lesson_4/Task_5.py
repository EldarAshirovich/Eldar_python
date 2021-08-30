import pydoc
from functools import reduce as r
"""
Autor Sabri Eldar

    5. Реализовать формирование списка, используя функцию range() и возможности генератора.
    В список должны войти чётные числа от 100 до 1000 (включая границы).
    Нужно получить результат вычисления произведения всех элементов списка.
    Подсказка: использовать функцию reduce().
"""

def myFunc(v1, v2):
    return v1 * v2
num_list = [x for x in range(100, 1001) if x % 2 == 0]
result = r(myFunc, num_list)
print(result)

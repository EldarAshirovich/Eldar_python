import pydoc

"""
Autor Sabri Eldar

    3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
    Решите задание в одну строку.
    Подсказка: используйте функцию range() и генератор.
"""

result_list = [x for x in range(20, 241) if ((x%20==0) or (x%21==0))]
print(result_list)

import pydoc
import json

"""
Autor Sabri Eldar

    7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
    Пример строки файла: firm_1 ООО 10000 5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
    Если фирма получила убытки, в расчет средней прибыли ее не включать.
    Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
    Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
    Итоговый список сохранить в виде json-объекта в соответствующий файл.
    Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
    Подсказка: использовать менеджеры контекста.
"""

with open("task_7.txt") as file:
    list = file.readlines()
str = "[{"
average_profit = 0
profit = 0
i2 = 0
for i, el in enumerate(list):
    new_list = el.split()
    summ = int(new_list[2]) - int(new_list[3])
    str += f'"{new_list[0]}":{summ}'
    if i+1 < len(list):
        str += f","
    if summ > 0:
        i2 += 1
        profit += int(summ)
str += "}"
profit = profit / i2
str += f', {{"average_profit": {profit:.2f}}}]'
with open('test_dict.json', 'w') as file:
    json.dump(json.loads(str), file)
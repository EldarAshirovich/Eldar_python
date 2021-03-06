import pydoc

"""
Autor Sabri Eldar

    6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
    практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
    Примеры строк файла:
    Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —

    Пример словаря:
    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

with open("task_6.txt") as file:
    list = file.readlines()
dict = {}
for el in list:
    new_list = el.split()
    summ = 0
    for i in range(1, 4):
        if new_list[i] != '—':
            num = ''.join([el for el in new_list[i] if el.isdigit()])
            summ += int(num)
    dict[new_list[0]] = summ
print(f"Общее количество занятий по предметам: {dict}")

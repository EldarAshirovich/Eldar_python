import pydoc

"""
Autor Sabri Eldar

    1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
    Об окончании ввода данных будет свидетельствовать пустая строка.
"""

in_str = 'Введите данные (для остановки введите пустую строку): '
while True:
    str = input(in_str)
    if str == '':
        with open("task_1.txt") as file:
            print("Вывод новых данных:")
            for line in file:
                print(line, end='')
            print("Скрипт окончен!")
        break
    else:
        try:
            with open("task_1.txt", 'a+') as file:
                file.write(str+'\n')
        except EOFError:
            print("Произошла ошибка ввода-вывода!")
        with open("task_1.txt") as file:
            print("Вывод новых данных:")
            for line in file:
                print(line, end='')

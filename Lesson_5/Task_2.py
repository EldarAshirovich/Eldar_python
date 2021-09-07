import pydoc

"""
Autor Sabri Eldar

    2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""

try:
    with open("task_1.txt") as file:
        for i, line in enumerate(file):
            print(f"Колчиество слов в строке(№{i+1}): {len(line.split())}, Количество символов в строке(№{i+1}): {len(line)}")
        print(f"Количество строк в файле: {i+1}")
except EOFError:
    print("Произошла ошибка ввода-вывода!")

import pydoc

"""
Autor Sabri Eldar

    5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

str = ''
summ = 0
for el in range(11):
    str += f"{el} "
    summ += el
print(f"Сумма чисел в фале: {summ}")
try:
    with open("task_5.txt", 'w+') as file:
        file.write(str)
except EOFError:
    print("Произошла ошибка ввода-вывода!")

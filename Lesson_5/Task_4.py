import pydoc

"""
Autor Sabri Eldar

    4. Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
    При этом английские числительные должны заменяться на русские. 
    Новый блок строк должен записываться в новый текстовый файл.
"""
dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
def funTranslate(el):
    return dict[el]
str = ''
with open("task_4.txt") as file:
    list = file.readlines()
for el in list:
    slt = el.split()
    str += f"{funTranslate(slt[0])} {slt[1]} {slt[2]}\n"
try:
    with open("task_4_new.txt", 'a+') as file:
        file.write(str)
except EOFError:
    print("Произошла ошибка ввода-вывода!")

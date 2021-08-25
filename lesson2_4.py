import pydoc
#Autor Sabri Eldar

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

in_txt = "Введите строку из нескольких слов: "
while True:
    usr_str = list(input(in_txt).split())
    l = len(usr_str)
    if l > 1:
        break
    else:
        print("Нужен хотя бы 1 пробел!!!")
for i, v in enumerate(usr_str):
    i+=1
    print(f"{i}. {v[:10]};")

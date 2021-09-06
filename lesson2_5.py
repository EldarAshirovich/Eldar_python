import pydoc
#Autor Sabri Eldar

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

in_txt = "Введите любое натуранльное число: "
reit_list = [7, 5, 3, 3, 2]
while True:
    try:
        usr_numb = int(input(in_txt))
        if str(usr_numb).isdigit() and float(usr_numb) == int(usr_numb) and int(usr_numb) > 0:
            # reit_list.append(usr_numb) старая реализация!
            # print(sorted(reit_list, reverse=True)) старая реализация!
            for el in range(len(reit_list)):
                if reit_list[0] < usr_numb:
                    reit_list.insert(0, usr_numb)
                    break
                elif reit_list[-1] > usr_numb:
                    reit_list.append(usr_numb)
                    break
                elif reit_list[el] < usr_numb and reit_list[el - 1] > usr_numb or reit_list[el] == usr_numb:
                    reit_list.insert(el, usr_numb)
                    break
            print(f"Список рейтинга - {reit_list}")
            if len(reit_list) > 10:
                break
        else:
            raise ValueError
    except ValueError:
        print("Неверный ввод! Введите натуральное число!")

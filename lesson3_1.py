import pydoc
#Autor Sabri Eldar

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

in_list_num = "Введите два числа через пробел: "
er_info = "Неверный ввод! Введите число!"
er_zero = "Деление на ноль не возможно!"
list_num = []
list_div = []
def chek_num(num):
    """
        Проверка на ввод числа.
        param: num(int, float)
        result: chek_res(int, float)
    """
    if str(num).isdigit() and int(num) > 0:
        chek_res = int(num)
    elif any(num.replace(x, '').isdigit() for x in ['.', ',']):
        num = num.replace(',', '.')
        chek_res = float(num)
    else:
        raise ValueError
    return chek_res
while True:
    try:
        list_num = input(in_list_num)
        list_num = list_num.split()
        if len(list_num) == 2:
            if int(list_num[1]) == 0:
                raise ZeroDivisionError
            else:
                for val in list_num:
                    list_div.append(chek_num(val))
                break
        else:
            print("Ошибка!!! Введите два числа через пробел!")
    except ZeroDivisionError:
        print(er_zero)
    except ValueError:
        print(er_info)
div_res = lambda x, y: x / y
print(f"Сумма деления чисел {list_div[0]:.2f} / {list_div[1]:.2f} = {div_res(list_div[0], list_div[1]):.2f}")

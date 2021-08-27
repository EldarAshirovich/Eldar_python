import pydoc
#Autor Sabri Eldar

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

in_txt = "Введите через пробел (символ стоп '0'): "
er_numb = "Вводите только числа."
er_list = "Нужен хотя бы 1 пробел."
stop = "0"
res = 0
exit = 0
while True:
	try:
		list_num = list(input(in_txt).split())
		l = len(list_num)
		if l > 1:
			for val in list_num:
				if str(val).isdigit() and float(val) == int(val) and int(val) >= 0:
					res += int(val)
					if (val) == "0":
						exit = 1
				else:
					raise ValueError
			print(f"Сумма чисел: {res}")
			if exit == True:
				break
		else:
			print(er_list)
	except ValueError:
		print(er_numb)

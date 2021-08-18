import pydoc
#Autor Sabri Eldar

#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
temp = []
def my_func(num_1, num_2, num_3):
	"""
		Сумма наибольших двух аргументов.
		param: num_1(int)
		param: num_2(int)
		param: num_3(int)
		result: res(str)
	"""
	if num_1>num_2 or num_1>num_3:
		temp.append(num_1)
	if num_2>num_1 or num_2>num_3:
		temp.append(num_2)
	if num_3>num_1 or num_3>num_2:
		temp.append(num_3)
	res = temp[0] + temp[1]
	res = f"Сумма наибольших двух аргументов из чисел: {num_1}, {num_2}, {num_3}\nЯвляется: {temp[0]} + {temp[1]} = {res}"
	return res

result = my_func(32, 7, 14)
print(result)

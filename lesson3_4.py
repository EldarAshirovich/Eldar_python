import pydoc
#Autor Sabri Eldar

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
	"""
		Возведение в отрицательную степень.
		param: x(int,float)
		param: y(int)
		return: res(str)
	"""
	res = ''
	temp = 1
	for i in range(abs(y)):
		if i+1 < len(range(abs(y))):
			res += f"{x} * "
		else:
			res += f"{x}"
		temp *= x
	if y <= 0:
		res += f" = {temp};\n1 / {temp} =  {1 / temp}"
		return res
print(my_func(4, -2))
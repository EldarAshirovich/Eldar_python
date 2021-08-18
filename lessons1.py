import pydoc
#Autor Sabri Eldar
print('{:-^100}\n'.format('Домашняя работа Сабри Эльдар'))

# Start Task 1 -------------------------------------------------------------------
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a_str = 'Строковый тип перемменной'
b_int = int('34')
c_f = float('36.25')
d_bool = True
f_dict = {"a_str": a_str, "b_int": b_int, "c_f": c_f, "d_bool": d_bool}
for k, v in f_dict.items():
	t = str(type(v))
	print(f"Переменная:{k:^10}  ->  Значение:{v:^30}  -> Тип:{t:^20}\n")
name = input('Введите ваше имя:')
age = int(input('Укажите ваш возраст:'))
print("Вы указали:\n  Ваше имя: {0};\n  Ваш возраст: {1};\n".format(name, age))
print('{:-^100}\n'.format('Конец задания!'))

End Task 1 ---------------------------------------------------------------------


Start Task 2 -------------------------------------------------------------------
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк.

in_txt = 'Введите время в секундах: '
while True:
	try:
		usr_numb = int(input(in_txt))
		if str(usr_numb).isdigit() and float(usr_numb) == int(usr_numb) and int(usr_numb) > 0:
			secs = usr_numb
			break
		else:
			raise ValueError
	except ValueError:
		print("Неверный ввод! Введите натуральное число!")
days = secs//86400
hours = (secs - days*86400)//3600
minutes = (secs - days*86400 - hours*3600)//60
seconds = secs - days*86400 - hours*3600 - minutes*60
result = ("{0:02}:{1:02}:{2:02}:{3:02}".format(days, hours, minutes, seconds))
print(result,"\n")
print('{:-^100}\n'.format('Конец задания!'))

# End Task 2 ---------------------------------------------------------------------


# Start Task 3 -------------------------------------------------------------------
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

in_txt = 'Ввдеите число: '
while True:
	try:
		usr_numb = int(input(in_txt))
		if str(usr_numb).isdigit() and float(usr_numb) == int(usr_numb) and int(usr_numb) > 0:
			n = usr_numb
			break
		else:
			raise ValueError
	except ValueError:
		print("Неверный ввод! Введите натуральное число!")
result = int(n) + int(n + n) + int(n + n + n)
print(f"Сумма {n}+{n+n}+{n+n+n}={result}\n")
print('{:-^100}\n'.format('Конец задания!'))

# End Task 3 ---------------------------------------------------------------------


# Start Task 4 -------------------------------------------------------------------
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

in_txt = 'Введите целое положительное число: '
while True:
	try:
		usr_numb = int(input(in_txt))
		if str(usr_numb).isdigit() and float(usr_numb) == int(usr_numb) and int(usr_numb) > 0:
			numb = usr_numb
			break
		else:
			raise ValueError
	except ValueError:
		print("Неверный ввод! Введите натуральное число!")
r = -1
while numb > 10:
    d = numb % 10
    numb //= 10
    if d > r:
        r = d
print(f"Наибольшая цифра в числе ({usr_numb}) - {r}\n")
print('{:-^100}\n'.format('Конец задания!'))

# End Task 4 ---------------------------------------------------------------------


# Start Task 5 -------------------------------------------------------------------
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

in_debit = "Введите дебет фирмы: "
in_credit = "Введите кредит фирмы: "
er_info = "Неверный ввод! Введите сумму!"
while True:
	try:
		debit = input(in_debit)
		if str(debit).isdigit() and int(debit) > 0:
			debit = int(debit)
			break
		elif any(debit.replace(x, '').isdigit() for x in ['.', ',']):
			debit = debit.replace(',', '.')
			debit = float(debit)
			break
		else:
			raise ValueError
	except ValueError:
		print(er_info)
while True:
	try:
		credit = input(in_credit)
		if str(credit).isdigit() and int(credit) > 0:
			credit = int(credit)
			break
		elif any(credit.replace(x, '').isdigit() for x in ['.', ',']):
			credit = credit.replace(',', '.')
			credit = float(credit)
			break
		else:
			raise ValueError
	except ValueError:
		print(er_info)
profit = debit - credit
print(f"{debit} - {credit} = {profit}")
if profit > 0:
	print("Фирма с прибылью!")
	rent = profit / debit * 100
	print(f"Рентабельность составляет: {rent:.2f} %")
	workers = int(input("Введите количество сотрудников фирмы:"))
	result = profit / workers
	print(f"Прибыль в расчете на одного сторудника сотавила: {result:.2f}руб.\n")
else:
	print("Фима в убытке!\n")
print('{:-^100}\n'.format('Конец задания!'))

# End Task 5 ---------------------------------------------------------------------


# Start Task 6 -------------------------------------------------------------------
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил
# a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

in_a = "Введите начальный результат бега: "
in_b = "Введите желаемый релультат бега за день: "
er_info = "Неверный ввод! Введите натуральное число!"
while True:
	try:
		a = input(in_a)
		if str(a).isdigit() and int(a) > 0:
			a = int(a)
			break
		elif any(a.replace(x, '').isdigit() for x in ['.', ',']):
			a = a.replace(',', '.')
			a = float(a)
			break
		else:
			raise ValueError
	except ValueError:
		print(er_info)
while True:
	try:
		b = input(in_b)
		if str(b).isdigit() and int(b) > 0:
			b = int(b)
			break
		elif any(b.replace(x, '').isdigit() for x in ['.', ',']):
			b = b.replace(',', '.')
			b = float(b)
			break
		else:
			raise ValueError
	except ValueError:
		print(er_info)
day = 0
while a < b:
	a *= 1.1
	day = day + 1
	print(f'{day}-й день: {a:.2f}')
	
print(f"На {day}-й день спортсмен достиг результата - не менее {b:.2f} км. \n")
print('{:-^100}\n'.format('Конец задания!'))

# End Task 6 ---------------------------------------------------------------------

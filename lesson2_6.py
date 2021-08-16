import pydoc
#Autor Sabri Eldar

# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
# product_arr = [(1, {"название": "принтер", "цена": 20000, "количество": 5, "eд": "шт."}),(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}), (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]

in_name = "Введите Наименовение товара: "
in_price = "Введите Цену товара: "
in_amo = "Введите Количество товара: "
in_unit = "Введите Еденицу измерения товара: "
er_price = "Неверный ввод! Введите цену!"
er_amo = "Неверный ввод! Введите количество!"
value = ''
anlc, list_harac = ({} for _ in range(2))
product_arr = [()]
i = 0
while True:
	v_name = input(in_name)
	while True:
		try:
			v_price = input(in_price)
			if str(v_price).isdigit() and int(v_price) > 0:
				break
			elif '.' in v_price or ',' in v_price:
				if any(v_price.replace(x, '').isdigit() for x in ['.', ',']):
					break
			else:
				raise ValueError
		except ValueError:
			print(er_price)
	while True:
		try:
			v_amo = input(in_amo)
			if str(v_amo).isdigit() and int(v_amo) > 0:
				break
			else:
				raise ValueError
		except ValueError:
			print(er_amo)
	v_unit = input(in_unit)
	product_arr[i] = (i+1, {"название": v_name, "цена": v_price, "количество": v_amo, "eд": v_unit})
	i += 1
	if i > 2:
		break
	product_arr.append(())
for k, v in product_arr:
	i = 1
	for k2, v2 in v.items():
		if k2 not in list_harac:
			list_harac[i] = str(k2)
			i+=1
for k, v in product_arr:
	i = 1
	for k2, v2 in list_harac.items():
		if v2 not in anlc:
			anlc[v2] = []
		if v2 == list_harac.get(i):
			if anlc[v2].count(v.get(v2)) == 0:
				value = str(v.get(v2))+" "
				anlc[v2] += value.split()
			i+=1
print(f'Результат аналитики товаров: {anlc}')

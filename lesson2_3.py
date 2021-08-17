import pydoc
#Autor Sabri Eldar

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

in_txt = "Введите месяц в виде целого числа от 1 до 12: "
while True:
	try:
		usr_numb = int(input(in_txt))
		if usr_numb < 1 or usr_numb > 12:
			raise ValueError
		break
	except ValueError:
		print("Неверный ввод! Введите число от 1 до 12!")
season_dict = {1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Лето', 7:'Лето', 8:'Лето', 9:'Осень', 10:'Осень', 11:'Осень', 12:'Зима'}
season_list = []
for i in season_dict.values():
	season_list.append(i)
print(f'Вывод через dict: {season_dict[usr_numb]}\nВывод через list: {season_dict[usr_numb]}')

import pydoc
#Autor Sabri Eldar

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, year, city, email, phone):
	"""
		Вывод данных о пользователе.
		param: name(str)
		param: surname(str)
		param: year(int)
		param: city(str)
		param: email(str)
		param: phone(str)
		result print_result(str)
	"""
	print_result = f"Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город проживания: {city}, Почта: {email}, Телефон: {phone}."
	return print_result

udd = {"name": "Eldar", "surname": "Sabri", "year": "1990", "city": "Simferopol", "email": "123@mail.ru", "phone": "+7(978) 123-47-58"}
result = user_data(udd["name"], udd["surname"], udd["year"], udd["city"], udd["email"], udd["phone"])
print(result)

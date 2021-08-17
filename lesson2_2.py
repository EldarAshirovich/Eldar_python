import pydoc
#Autor Sabri Eldar

# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

in_txt = "Введите значения списка через пробел: "
while True:
	usr_list = list(input(in_txt).split())
	l = len(usr_list)
	if l > 1:
		break
	else:
		print("Нужно указать больше 1 значения в списке!!!")
new_list = usr_list.copy()
i = 0
if l%2 == 1:
	l = l - 1
while i < l:
	n = i % 2
	if n == 0:
		new_list[i+1] = usr_list[i]
	else:
		new_list[i-1] = usr_list[i]
	i+=1
print(f"Пользовательский список  : {usr_list}")
print(f"Список с обменом значений: {new_list}")

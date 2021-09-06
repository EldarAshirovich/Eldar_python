import pydoc

"""
Autor Sabri Eldar

    1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
    Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
    Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

    31  22      |       3   5   32      |       3   5   8   3
    37  43      |       2   4   6       |       8   3   7   1
    51  86      |       -1  64  -8      |       

    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица. 
    Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    
    def __init__(self, list_of_list):
        self.matrix = list_of_list
    
    def __str__(self):
        result = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result += '{: ^5}'.format(self.matrix[i][j])
            result += '\n'
        return result
    
    def __add__(self, other):
        result = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result += '{: ^5}'.format(self.matrix[i][j] + other.matrix[i][j])
            result += '\n'
        return result

list_of_list_1 = [[31, 22], [37, 43], [51, 86]]
list_of_list_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
list_of_list_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]
list_of_list_4 = [[12, 27], [23, 71], [32, -15]]

print('{:-^50}\n'.format("Вывод матрицы №1 (3х2)"))
print(Matrix(list_of_list_1))
print('{:-^50}\n'.format("Вывод матрицы №2 (3х3)"))
print(Matrix(list_of_list_2))
print('{:-^50}\n'.format("Вывод матрицы №3 (2х4)"))
print(Matrix(list_of_list_3))
print('{:-^50}\n'.format("Вывод матрицы №4 (3х2)"))
print(Matrix(list_of_list_4))
print('{:-^50}\n'.format("Сложение матриц №1 + №4 (3x2)"))
list_of_list_5 = Matrix(list_of_list_1) + Matrix(list_of_list_4)
print(list_of_list_5)
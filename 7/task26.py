# #todo Задача 1. Чтение матрицы, load_matrix(filename)
# # Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)
#
# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36
#
#
# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.
#
# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!
from fileinput import filename


filename = "task26filename.txt"

def load_matrix(filename):
    with open(filename, encoding='utf-8') as f:
        matrix = [[int(x) for x in line.split()] for line in f]
        print(matrix)
    return matrix if matrix and all(
        [len(row) > 0 and len(row) == len(matrix[0]) for row in matrix]
    ) else False

if __name__ == '__main__':
    result = load_matrix(filename)

    if result:
        print(*[' '.join(map(str, row)) for row in result], sep='\n')
    else:
        print(result)
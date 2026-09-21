#todo: Дан массив размера N. Найти минимальное расстояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
#
#
# Для числа 1 минимальное расстояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное расстояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального расстояния т.к элемент в массиве один.


def find_min_distances(arr):
    last_index = {}          # хранит последний индекс каждого значения
    min_dist = {}            # минимальное расстояние для каждого значения
    pair_indices = {}        # пара индексов, на которых достигается минимальное расстояние

    for i, val in enumerate(arr):
        if val in last_index:
            prev_i = last_index[val]
            dist = i - prev_i

            # Если это первое повторное вхождение или нашли меньшее расстояние
            if val not in min_dist or dist < min_dist[val]:
                min_dist[val] = dist
                pair_indices[val] = (prev_i, i)

        # Обновляем последний индекс текущего значения
        last_index[val] = i

    return min_dist, pair_indices


# Пример из задачи
mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]

min_dist, pair_indices = find_min_distances(mass)

for val in sorted(min_dist.keys()):
    dist = min_dist[val]
    i1, i2 = pair_indices[val]
    print(f"Для числа {val} минимальное расстояние: {dist}, индексы: {i1} и {i2}")
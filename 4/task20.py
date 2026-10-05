#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# # Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.




# Открываем файл для чтения
with open('inverted_sort.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Открываем файл для дозаписи в конец ('a' — append)
with open('inverted_sort.txt', 'a', encoding='utf-8') as f:
    # reversed() возвращает строки в обратном порядке
    for line in reversed(lines):
        f.write(line)

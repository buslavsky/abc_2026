#todo: Модифицировать программу таким образом чтобы она выводила
# приветствие "Hello", которое только что записали в файл text.txt

# f = open("text.txt", "w+t")
# f.write("Hello\n")
# Ваше решение.

# f.close()
#

f = open("text.txt", "w+t")
f.write("Hello\n")

f.seek(0)              # возвращаем курсор в начало файла
content = f.read()     # читаем всё содержимое
print(content, end="") # Hello

f.close()

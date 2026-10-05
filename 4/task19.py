#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
#              "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
#              "Наивный байесовский классификатор", "CART" ]

# Каждое значение из списка должно находится на отдельной строке.
# Пример файла algoritm.csv:
#1) "C4.5"
#2) "k - means"
#.....

import csv

algoritm = ["C4.5", "k - means", "Метод опорных векторов",
            "Apriori", "EM", "PageRank", "AdaBoost", "kNN",
            "Наивный байесовский классификатор", "CART"]

# Создаем и записываем данные в CSV-файл
with open('algoritm.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Записываем заголовки столбцов
    writer.writerow(['id', 'значение из списка algoritm'])
    
    # Записываем данные (номер по порядку и значение)
    for i, alg in enumerate(algoritm, start=1):
        writer.writerow([i, alg])

print("Файл algoritm.csv успешно создан!")
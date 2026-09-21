# # todo: База данных пользователя.
# # Задан массив объектов пользователя
#
# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введённого) ,первой букве логина, и заданной группе.
#
# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
#
# #Затем сообщение для ввода
# Введите критерии поиска: 16
#
# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [
    {'login': 'Piter', 'age': 23, 'group': "admin"},
    {'login': 'Ivan', 'age': 10, 'group': "guest"},
    {'login': 'Dasha', 'age': 30, 'group': "master"},
    {'login': 'Fedor', 'age': 13, 'group': "guest"}
]


def get_sort_type():
    print("Тип сортировки:")
    print("1. По возрасту")
    print("2. По первой букве логина")
    print("3. По группе")

    while True:
        try:
            choice = int(input("Введите тип сортировки (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Пожалуйста, введите число от 1 до 3.")
        except ValueError:
            print("Нужно ввести число.")


def filter_and_sort_users():
    sort_type = get_sort_type()

    # Определяем поле и логику фильтрации/сортировки
    if sort_type == 1:  # По возрасту (больше введённого)
        field = 'age'
        try:
            threshold = int(input("Введите критерии поиска (минимальный возраст): "))
        except ValueError:
            print("Некорректное значение возраста.")
            return

        filtered = [u for u in users if u['age'] > threshold]
        # Сортируем по возрасту по возрастанию
        result = sorted(filtered, key=lambda x: x['age'])

    elif sort_type == 2:  # По первой букве логина
        field = 'login'
        prefix = input("Введите первую букву логина: ").strip().lower()
        if not prefix:
            print("Буква не введена.")
            return

        filtered = [u for u in users if u['login'].lower().startswith(prefix)]
        # Сортируем по логину (алфавитно)
        result = sorted(filtered, key=lambda x: x['login'])

    else:  # sort_type == 3, по группе
        field = 'group'
        target_group = input("Введите название группы: ").strip()
        filtered = [u for u in users if u['group'] == target_group]
        # Сортируем по логину внутри группы (для порядка)
        result = sorted(filtered, key=lambda x: x['login'])

    # Вывод результата в требуемом формате
    if not result:
        print("Подходящих пользователей не найдено.")
        return

    for user in result:
        login = user['login']
        age = user['age']
        group = user['group']
        # Формируем строку как в примере: "Пользователь: 'Piter' возраст 23 года , группа  "admin""
        print(f"Пользователь: '{login}' возраст {age} года/лет , группа \"{group}\"")


# Запуск
filter_and_sort_users()

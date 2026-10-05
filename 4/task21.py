# #todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# # нужно сопоставить данные для подстановки.
#
# # Содержимое файла config_default.txt
# # Конфигурация приложения.
# app_name    = ?
# version     = ?
# debug       = ?
#
# # Настройки базы данных
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?
#
# # Настройки API
# api_key     = ?
# api_secret  = ?
# base_url    = ?
#
# # Пути
# log_file    = ?
# data_dir    = ?
# temp_dir    = ?
#
#
# # Данные для подстановки
# config_values = {
#     'app_name': 'NextGen',
#     'version': '1.0.0',
#     'debug':  True,
#     'db_host': 'localhost',
#     'db_port': 5432,
#     'db_name': 'my_database',
#     'db_user': 'admin',
#     'db_password': 'secret123',
#     'api_key': 'ak_123456789',
#     'api_secret': 'sk_987654321',
#     'base_url': 'https://api.example.com',
#     'log_file': '/var/log/app.log',
#     'data_dir': '/opt/app/data',
#     'temp_dir': '/tmp/app',
#     'max_workers': 10,
#     'timeout': 30,
#     'retry_attempts': 3
# }
#
# # В итоге вместо "?" должны подставиться значения и получиться файл config.txt:
#
# # Конфигурация приложения
# app_name    =  "NextGen"
# version     =  '1.0.0'
# debug       =  True
#
# # Настройки базы данных
# db_host     =  5432
# .....

# Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug': True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}


def format_value(value):
    """Форматирует значение для подстановки в конфиг."""
    if isinstance(value, bool):
        # True/False без кавычек
        return str(value)
    if isinstance(value, (int, float)):
        # Числа без кавычек
        return str(value)
    # Строки в двойных кавычках
    return f'"{value}"'


def render_config(template_path, output_path, values):
    with open(template_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result_lines = []
    missing = set()

    for line in lines:
        # Ищем строки вида "key = ?"
        if '=' in line and '?' in line:
            key_part, _, value_part = line.partition('=')
            key = key_part.strip()

            if value_part.strip() == '?' and key in values:
                new_value = format_value(values[key])
                # Сохраняем выравнивание: заменяем "?" на значение
                result_lines.append(
                    line.replace('?', new_value, 1)
                )
                continue

            if value_part.strip() == '?' and key not in values:
                missing.add(key)

        result_lines.append(line)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(result_lines)

    if missing:
        print(f"Предупреждение: нет значений для ключей: {sorted(missing)}")
    else:
        print(f"Файл {output_path} успешно создан.")


if __name__ == '__main__':
    render_config('config_default.txt', 'config.txt', config_values)

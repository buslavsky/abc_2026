# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.
#
# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

def caesar_cipher(text, shift):
    """
    Шифрует текст шифром Цезаря с заданным сдвигом влево.
    Шифрует только буквы кириллицы.
    """
    # Русский алфавит (заглавные и строчные буквы)
    uppercase = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    result = []
    
    for char in text:
        if char in uppercase:
            # Находим индекс символа в алфавите
            index = uppercase.index(char)
            # Сдвигаем влево на shift позиций (с цикличностью)
            new_index = (index - shift) % len(uppercase)
            result.append(uppercase[new_index])
        elif char in lowercase:
            index = lowercase.index(char)
            new_index = (index - shift) % len(lowercase)
            result.append(lowercase[new_index])
        else:
            # Не буквы кириллицы оставляем без изменений
            result.append(char)
    
    return ''.join(result)


def encrypt_file(input_file, output_file):
    """
    Читает файл построчно и шифрует каждую строку с увеличивающимся сдвигом.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for i, line in enumerate(lines, start=1):
                # Сдвиг равен номеру строки (первая строка - сдвиг 1, вторая - 2 и т.д.)
                encrypted_line = caesar_cipher(line, i)
                f.write(encrypted_line)
        
        print(f"Файл успешно зашифрован и сохранён как {output_file}")
    
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")
    except Exception as e:
        print(f"Ошибка: {e}")


# Основная программа
if __name__ == "__main__":
    encrypt_file('message.txt', 'encrypted.txt')

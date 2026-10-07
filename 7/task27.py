# #todo:
# 1. Создайте виртуальное окружение через терминал в текущей папки нового проекта.
# Название окружению дайте по названию проекта. Переключитесь на созданное новое окружение.
#
# 2. Установите пакет pandas.
# Убедитесь что он установился и добавился в папку виртуального окружения.
#
#
# 3. Создайте файл test_package.py в него добавьте строки
#
# import pandas as pd
# pd.test()
#
# Убедитесь что пакет подкючен.
#
# 4. Создайте свой пакет helpers со структурой
#
# helpers
#     __init__.py
#     io.py
#     crypt.py
#
# В модуль io.py разместите ранее написаный logger
# В модуль crypt.py добавьте функцию шифра цезаря.
#
# 5. Создайте новый файл test.py  Подключите в него функцию логера и шифрования.
# Проверьте их работу.

# Пошаговое решение

## 1. Виртуальное окружение

#Откроем терминал, перейдём в папку проекта (пусть проект называется `my_project`):

#```bash
mkdir my_project
cd my_project

# создаём окружение с именем проекта
python -m venv my_project

# активируем
# Windows:
#my_project\Scripts\activate
# Linux / macOS:
source my_project/bin/activate
#```

#После активации в начале строки терминала появится `(my_project)`.
## 2. Установка pandas
#```bash
pip install pandas
#```

#Проверка, что пакет установился в окружение:

#```bash
pip show pandas
# Location: ...\my_project\Lib\site-packages
#```

#Также убедиться можно, заглянув в `my_project/Lib/site-packages` — там должна появиться папка `pandas`.

## 3. Файл `test_package.py`
#```python
import pandas as pd

pd.test()
#```

#Запуск:
#```bash
python test_package.py
#```
#Если в выводе нет ошибок про импорт — пакет подключён корректно.

## 4. Свой пакет `helpers`
#Структура:
#```
# helpers/
#     __init__.py
#     io.py
#     crypt.py
# ```

#helpers/io.py — логгер:

#```python
import logging

def get_logger(name: str = 'app', filename: str = 'app.log') -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fmt = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

        fh = logging.FileHandler(filename, encoding='utf-8')
        fh.setFormatter(fmt)

        sh = logging.StreamHandler()
        sh.setFormatter(fmt)

        logger.addHandler(fh)
        logger.addHandler(sh)
    return logger
#```

#`helpers/crypt.py` — шифр Цезаря:

#```python
def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    """Шифр Цезаря. decrypt=True — расшифровка."""
    if decrypt:
        shift = -shift

    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)
#```

#`helpers/__init__.py` — реэкспорт:

#```python
from .io import get_logger
from .crypt import caesar_cipher

__all__ = ['get_logger', 'caesar_cipher']
#```

## 5. Файл `test.py`

#```python
from helpers import get_logger, caesar_cipher

logger = get_logger('test')

logger.info('Программа запущена')

original = "Hello, World!"
encrypted = caesar_cipher(original, 3)
decrypted = caesar_cipher(encrypted, 3, decrypt=True)

logger.info(f'Оригинал:  {original}')
logger.info(f'Шифр:      {encrypted}')
logger.info(f'Расшифровка: {decrypted}')

assert decrypted == original
logger.info('Проверка пройдена')
#```

#Запуск:

#```bash
python test.py
#```

#Ожидаемый вывод в консоли (и в файле `app.log`):

#```
# ... | INFO | Программа запущена
# ... | INFO | Оригинал:  Hello, World!
# ... | INFO | Шифр:      Khoor, Zruog!
# ... | INFO | Расшифровка: Hello, World!
# ... | INFO | Проверка пройдена
# ```

## Итоговое дерево проекта

#```
# my_project/
# ├── my_project/          # виртуальное окружение
# ├── helpers/
# │   ├── __init__.py
# │   ├── io.py
# │   └── crypt.py
# ├── test_package.py
# └── test.py
# ```
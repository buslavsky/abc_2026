# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

# Пример использования
# user = User("test@example.com", "secret")
# print(user.email)  # test@example.com
# # print(user.password) # AttributeError
# print(user.check_password("secret"))  # True
# print(user.check_password("wrong"))   # False

class User:
    def __init__(self, email: str, password: str):
        # используем сеттеры для валидации
        self.email = email
        self.password = password

    # ---------- email ----------
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if not isinstance(value, str) or '@' not in value:
            raise ValueError('Некорректный email: должен содержать символ "@"')
        self._email = value

    # ---------- password ----------
    @property
    def password(self):
        # Свойство только для записи: чтение запрещено
        raise AttributeError('Чтение пароля запрещено')

    @password.setter
    def password(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError('Пароль должен быть непустой строкой')
        self._password_hash = hash(value)

    # ---------- проверка ----------
    def check_password(self, password: str) -> bool:
        return hash(password) == self._password_hash

    def __repr__(self) -> str:
        return f'User(email={self._email!r})'


# ---------- Пример использования ----------
if __name__ == '__main__':
    user = User("test@example.com", "secret")
    print(user.email)                     # test@example.com
    # print(user.password)                # AttributeError
    print(user.check_password("secret"))  # True
    print(user.check_password("wrong"))   # False

    # проверка валидации email
    try:
        user.email = "invalid"
    except ValueError as e:
        print('Ошибка:', e)                # Ошибка: Некорректный email: должен содержать символ "@"


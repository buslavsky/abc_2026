# Инкапсуляция и property
# todo: Класс "Температура"
# Создайте класс Temperature, который хранит температуру в градусах Цельсия.
# Добавьте свойство для получения и установки температуры в Фаренгейтах и Кельвинах.
# Внутренне температура должна храниться только в Цельсиях.

# celsius (get, set) - работа с Цельсиями.
# fahrenheit (get, set) - при установке конвертирует значение в Цельсии.
# kelvin (get, set) - при установке конвертирует значение в Цельсии.

# Пример использования
# t = Temperature(25)
# print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
# t.fahrenheit = 32
# print(f"После установки 32F: {t.celsius}C")

class Temperature:
    def __init__(self, celsius: float = 0.0):
        # внутреннее хранилище — только Цельсии
        self._celsius = 0.0
        self.celsius = celsius

    # ---------- Цельсии ----------
    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError('Температура не может быть ниже абсолютного нуля')
        self._celsius = float(value)

    # ---------- Фаренгейты ----------
    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        # F -> C : (F - 32) * 5/9
        self.celsius = (value - 32) * 5 / 9

    # ---------- Кельвины ----------
    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float):
        # K -> C : K - 273.15
        self.celsius = value - 273.15

    def __repr__(self) -> str:
        return f'Temperature(celsius={self._celsius})'


# ---------- Пример использования ----------
if __name__ == '__main__':
    t = Temperature(25)
    print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
    # 25.0C, 77.0F, 298.15K

    t.fahrenheit = 32
    print(f"После установки 32F: {t.celsius}C")
    # После установки 32F: 0.0C

    t.kelvin = 300
    print(f"После установки 300K: {t.celsius}C, {t.fahrenheit}F")
    # После установки 300K: 26.85C, 80.33F
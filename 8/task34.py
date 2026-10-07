# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.

# Пример использования
# book = Product("Book", 10)
# pen = Product("Pen", 2)
# order = Order()
# order.add_product(book)
# order.add_product(pen)
# print(f"Общая стоимость: {order.total_price}")  # 12

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = max(0, value)  # or if value < 0: self._price = 0 else value


class Order:
    def __init__(self):
        self._products = []  # encapsulate list

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)
        # maybe raise error if not found? Not specified. We can just remove if present.

    @property
    def total_price(self):
        return sum(p.price for p in self._products)

# Класс Product из предыдущей задачи (для полноты примера)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # проходит через сеттер

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            self._price = 0
        else:
            self._price = value


class Order:
    def __init__(self):
        # Приватный список товаров (инкапсуляция)
        self._products = []

    def add_product(self, product):
        """Добавляет товар в заказ."""
        self._products.append(product)

    def remove_product(self, product):
        """Удаляет товар из заказа, если он там есть."""
        if product in self._products:
            self._products.remove(product)
        # Если товара нет — ничего не делаем (можно было бы бросить исключение)

    @property
    def total_price(self):
        """Вычисляемое свойство: сумма цен всех товаров в заказе."""
        return sum(p.price for p in self._products)


# Пример использования
book = Product("Book", 10)
pen = Product("Pen", 2)

order = Order()
order.add_product(book)
order.add_product(pen)

print(f"Общая стоимость: {order.total_price}")  # 12

# Проверка удаления
order.remove_product(pen)
print(f"После удаления ручки: {order.total_price}")  # 10
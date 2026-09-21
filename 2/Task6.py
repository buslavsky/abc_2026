# Функция для считывания стороны квадрата от пользователя
def get_side():
    try:
        a = float(input("Введите сторону квадрата (положительное число): "))
        if a <= 0:
            raise ValueError("Сторона квадрата должна быть положительным числом!")
        return a
    except ValueError:
        print("Пожалуйста, введите корректное положительное число.")
        return get_side()  # Повторяем запрос до получения годного значения

# Функция для вычисления площади квадрата
def calculate_area(side):
    return side ** 2

side = get_side()
area = calculate_area(side)
print(f"\nПлощадь квадрата со стороной {side} равна {area}")
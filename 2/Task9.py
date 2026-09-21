# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

# Функция для считывания коэффициентов уравнения
def get_coefficients():
    while True:
        try:
            A = float(input("Введите коэффициент A (не равный нулю): "))
            if A == 0:
                print("Коэффициент A не должен быть равен нулю!")
                continue

            B = float(input("Введите коэффициент B: "))
            return A, B
        except ValueError:
            print("Пожалуйста, введите корректные числовые значения для A и B.")


# Функция для решения линейного уравнения
def solve_linear_equation(A, B):
    x = -B / A
    return x


# Основная программа
def main():
    try:
        A, B = get_coefficients()
        solution = solve_linear_equation(A, B)
        print(f"\nУравнение {A}x + {B} = 0 решено.")
        print(f"Корень уравнения: x = {solution}")
    except ValueError as e:
        print(f"Произошла ошибка: {e}")


main()
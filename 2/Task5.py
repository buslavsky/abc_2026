#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

def read_from_console():
    global first, second
    first = input("Введите первое число:\n")
    #global second
    second = input("Введите второе число:\n")
    print (f"Ваше первое число A = {first}")
    print (f"Ваше второе число B  = {second}")

def get_numbers():
    global first, second
    try:
        first = float(input("Введите первое число: "))
        second = float(input("Введите второе число: "))
        return first, second
    except ValueError:
        print(f"Пожалуйста, введите корректные числовые значения.")
        return get_numbers()  # Рекурсивный вызов для повторного ввода

def show_explanation_text():
    print (f"Результаты операций над Вашими числами")

def count_sum():
    summ = int(first) + int(second)
    print (f"Сумма A + B = {summ}")

def count_difference():
    diff = int(first) - int(second)
    print (f"Разность A - B = {diff}")

def count_multiply():
    multiply = float(int(first)  * int(second))
    print (f"Произведение A*B = {multiply}")

# Функция для проверки деления на ноль
def safe_division(first, second):
    if second == 0:
        raise ValueError("Деление на ноль невозможно!")
    return int(first) / int(second)

def count_quotient():
    if second == 0:
        print("На ноль делить нельзя, результата нет")
        raise ValueError("Деление на ноль невозможно!")
    else:
        quotient = float(int(first)  / int(second))
        print (f"Частное A/B = {quotient}")

def integer_division(first:int, second:int):
    int_div = int(first) // int(second)
    print (f"Целочисленное деление = {int_div}")

def calculate_power(first, second):
    power = int(first) ** int(second)
    print (f"Целочисленное деление = {power}")



#read_from_console()
get_numbers()
show_explanation_text()
count_sum()
count_difference()
count_multiply()
safe_division(first, second)
count_quotient()
integer_division(first, second)




# #todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

def numbers_to_letters(s: str) -> str:
    result = []
    for token in s.split():
        if token.isdigit():
            n = int(token)
            if n == 0:
                result.append(" ")
            else:
                result.append(chr(ord("a") + n - 1))
        else:
            result.append(token)
    return "".join(result)


print(numbers_to_letters("8 5 12 12 15"))
# hello

print(numbers_to_letters("8 5 12 12 15 , 0 23 15 18 12 4 !"))
# hello, world!
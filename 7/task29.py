# #todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

import string

cipher = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

def decrypt_caesar(text, shift):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    result = []

    for ch in text:
        if ch in lower:
            result.append(lower[(lower.index(ch) - shift) % 26])
        elif ch in upper:
            result.append(upper[(upper.index(ch) - shift) % 26])
        else:
            result.append(ch)

    return ''.join(result)

for shift in range(26):
    print(shift, decrypt_caesar(cipher, shift))
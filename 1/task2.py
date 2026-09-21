# проверялось на Python 3.10

# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
age = "23"
foo = "23abc"

age = int(age)
#вывод 25, но строка останется строкой
type(age)
#<class 'str'>

#приводим foo к хексу, т.к. и цифры, и буквы, подходят
foo = "23abc"
foo = int(foo, 16)
type(foo)
#<class 'int'>

#
# Преобразуйте переменную age в Boolean
# age = "123abc"
age = "123abc"
age = bool(age)
type(age)
# True


# Преобразуйте переменную flag в Boolean
# flag = 1
flag = 1
flag = bool(flag)
type(flag)
#True

# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
 str_one = "Privet"
 str_two = ""
 str_one = bool(str_one)
 str_two = bool(str_two)
 
type(str_one)
# <class 'bool'>
type(str_two)
# <class 'bool'>

# Преобразуйте значение 0 и 1 в Boolean
bool(0)
#False
bool(1)
#True

# Преобразуйте False в строку
boolean_value = False
string_value = str(boolean_value)

print(string_value)
# False
print(type(string_value))
# <class 'str'>
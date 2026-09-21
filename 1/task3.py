# todo: Данные две переменные:
# age = 36.6
# temperature = 25
# Нужно обменять значения переменных местами. В итого age
# должен равнятся 25 а temperature – 36.6:
age = 36.6
temperature = 25
temp = age
age = temperature
temperature = temp
print(age)
# 25
print(temperature)
# 36.6

# ИЛИ

age = 25
temperature = 36.6
(age, temperature) = (temperature, age)
print(age)
#36.6
print(temperature)
#25
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму
# двух целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

first_numb = int(input("Введите первое число: "))
second_numb = int(input("Введите второе число: "))

def sum(first_numb, second_numb):
    if second_numb == 0:
        return first_numb
    return sum(first_numb+1,second_numb-1)

print(f"Сумма = {sum(first_numb,second_numb)}")    
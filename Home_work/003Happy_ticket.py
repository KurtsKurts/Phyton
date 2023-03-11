# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

Happy_ticket = int(input('Введите номер билета : '))

numb6 = int(Happy_ticket % 10)
numb5 = int(Happy_ticket % 100/10)
numb4 = int(Happy_ticket % 1000/100)
sum_second_3 = int(numb6+numb5+numb4)
first_3 = int(Happy_ticket/1000)
numb3 = int(first_3 % 10)
numb2 = int(first_3 % 100/10)
numb1 = int(first_3 % 1000/100)
sum_first_3 = int(numb3+numb2+numb1)
if int (sum_first_3 == sum_second_3):
    print(f'{Happy_ticket} -> yes')
else : print(f'{Happy_ticket} -> no')

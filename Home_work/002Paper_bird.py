# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

Paper_bird = int(input('Введите количество бумажных журавликов : '))

Petia_bird = int(Paper_bird / 6)
Sergey_bird = int(Paper_bird / 6)
Katia_birg = int((Petia_bird + Sergey_bird) * 2)

print(f'Из {Paper_bird} журавликов Петя сделал-> {Petia_bird} Сергей сделал-> {Sergey_bird} и Катя сделала-> {Katia_birg}')

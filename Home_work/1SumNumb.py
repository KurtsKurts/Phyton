# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

Tree_numb=int(input('Введите трехзначное число : '))

sum = int(Tree_numb%10 + Tree_numb%100/10 + Tree_numb%1000/100)
print(f'Сумма цифр трехзначного числа = {sum}')
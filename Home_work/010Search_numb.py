# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random


number = int(input("Введите число для поиска: "))
my_list = [random.randint(0,10) for _ in range(30)]
print(my_list)
count = 0
closet_num = None
min_d = max(my_list)
for items in my_list:
    if number == int(items):
        count += 1
    elif abs(number-items) < min_d:
        min_d= abs(number-items)
        closet_num= items


if count == 0:
     print(f"Самое близкое значение = {closet_num}")
else: print(f"Число {number} встречается {count} раз/раза ")
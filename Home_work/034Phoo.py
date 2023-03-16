# phoo_song = input("Введите стих: ")
# parse_song = list(phoo_song.split("-"))
# my_dict = {"у", "е", "ё", "ы", "а", "о", "э", "я", "и", "ю"}
# count = 0
# song = True

# for el in parse_song:
#     for buk in el:
#         for glas in my_dict:
#             if buk == glas:
#                 count+=1
#     if count % 2 != 0:
#         song = False
#         break               
# if song:
#     print("Парам пам-пам")
# else: print("Пам парам")

def word(words):
    str = words.lower().split()
    f = lambda x: sum(1 for i in x if i in 'аоуыэеёиюя')
    tmp = f(str[0])
    if all([f(i) == tmp for i in str]):
        return 'Парам пам-пам'
    return 'Пам парам'


print(word("пара-ра-рам рам-пам-папам па-ра-па-да"))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]


# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)


# song_number = input('Введите индексы 3х песен через запятую ').split(',')
text_1 = 'Введите индекс песни №1_ от 0 до ' + str(len(violator_songs_list)-1)
text_2 = 'Введите индекс песни №2_ от 0 до ' + str(len(violator_songs_list)-1)
text_3 = 'Введите индекс песни №3_ от 0 до ' + str(len(violator_songs_list)-1)
print(text_1)
song_1 = input()
print(text_2)
song_2 = input()
print(text_3)
song_3 = input()

song_adder = song_counter = 0
if song_1.isdigit() and song_2.isdigit() and song_3.isdigit():
    while song_counter < len(violator_songs_list):
        if song_counter == int(song_1):
            song_adder = song_adder + violator_songs_list[song_counter][1]
        elif song_counter == int(song_2):
            song_adder = song_adder + violator_songs_list[song_counter][1]
        elif song_counter == int(song_3):
            song_adder = song_adder + violator_songs_list[song_counter][1]
        song_counter += 1
    if int(song_1) >= len(violator_songs_list) or int(song_2) >= len(violator_songs_list) or int(song_3) >= len(violator_songs_list):
        print('Ошибка! Индекс песни не может быть больше', len(violator_songs_list)-1)
    else:
        print('Время звучания 3х песен =', round(song_adder), 'минут')
else: print('Ошибка! Индекс должен быть числом!')


# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут



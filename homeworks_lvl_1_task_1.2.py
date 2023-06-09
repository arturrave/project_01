# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут


import random

print("Пункт А: ")

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

song_time = 0


for i in range(3):
    random_song_index = random.randrange(0,8)
    print(my_favorite_songs[random_song_index], my_favorite_songs[random_song_index][1] )
    song_time = song_time + my_favorite_songs[random_song_index][1]


print ("Три песни звучат", song_time, 'минут')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.


print('Пункт Б: ')

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

song_time_in_dict = 0



for i in range(3):
    random_song_key = random.choice(list(my_favorite_songs_dict))
    print(random_song_key, my_favorite_songs_dict[random_song_key])
    song_time_in_dict = song_time_in_dict + my_favorite_songs_dict[random_song_key]




print ("Три песни звучат", song_time_in_dict, 'минут')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

print('Дополнительно для пунктов A и B: ')

random_list = random.randint(0, len(my_favorite_songs) - 1)

print('Случайный трек: ', my_favorite_songs[random_list])


# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

print('Дополнительно. Пункт D: ')

import datetime



for i in range(0, len(my_favorite_songs)):
    song_lenght = my_favorite_songs[i][1]
    result = str(datetime.timedelta(minutes=song_lenght))
    sep = '.'
    stripped = result.split(sep, 1)[0]
    print('Длина трека: ', my_favorite_songs[i][0], 'составляет: ', stripped)
    




    
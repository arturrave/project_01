# Задача 1.1.

# Есть строка с перечислением песен

#my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.



# Узнаем порядковый номер каждого символа в строке, для этого воспользуемся циклом for и функцией enumerate() :

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
#for i in enumerate(my_favorite_songs):
#    print(i) 



print ("Первый трек: ", my_favorite_songs[:14],
        "Последний трек: ", my_favorite_songs[64:],
          "Второй трек: ", my_favorite_songs[16:30],
          # Узнаем порядковый номер символов с конца строки:
          #for i in enumerate(my_favorite_songs[::-1]):
          #print(i)
          # Поехали:
           "Второй трек с конца: ", my_favorite_songs [-61:-47])



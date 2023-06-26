# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    text = ''
    for i in s:
        if i != '!':
            text = text + i
            
    return text 

print(remove_exclamation_marks('Hi! Hello!'))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    text = ''
    last_index = len(s)
    if s[last_index - 1] == '!':
        text = s[:-1]
        return text
    else:
        return s    
    

print(remove_last_em('Hi!!'))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    words = s.split()
    alter_words = []

    for i in words:
      original_leght = len(i)
      new_i = i.replace('!', '')
      transform_lenght = len(new_i)
      delta = original_leght - transform_lenght
      
      if delta != 1:
        alter_words.append(i)

    return ' '.join(alter_words)


print(remove_word_with_one_em("Hi! !Hi! Hi!"))
print(remove_word_with_one_em("Hi! Hi!! Hi!"))
print(remove_word_with_one_em("Hi! Hi! Hi!"))
print(remove_word_with_one_em("Hi Hi! Hi!"))
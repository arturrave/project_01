# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

month_list = [
 'январь',
 'февраль',
 'март',
 'апрель',
 'май',
 'июнь',
 'июль',
 'август',
 'сентябрь',
 'октябрь',
 'ноябрь',
 'декабрь'
 ]

def quarter_of(month_number):
    month= month_list[month_number-1]
    if month_number <= 0 or month_number > 12:
        return 'Недопустимое значение'
        
    if month_number > 0 and month_number < 4:
        return f'месяц {month_number} ({month}) является частью первого квартала' 
    if month_number > 3 and month_number < 7:
        return f'месяц {month_number} ({month}) является частью второго квартала'
    if month_number > 6 and month_number < 10:
        return f'месяц {month_number} ({month}) является частью третьего квартала'
    if month_number > 9 and month_number < 13:
        return f'месяц {month_number} ({month}) является частью четвертого квартала'

print(quarter_of(2))  


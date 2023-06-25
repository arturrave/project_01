# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3

# Создаем таблицу студентов
sqlite_connection = sqlite3.connect("teatchers.db")

create_table_query = '''CREATE TABLE Students (
                                Student_Id INTEGER,
                                Student_Name TEXT NOT NULL,
                                School_Id INTEGER PRIMARY KEY
                                );'''

cursor = sqlite_connection.cursor()

try:
  cursor.execute(create_table_query)
except sqlite3.Error as error:
     print("Ошибка при работе с SQLite:", error)

# Заполняем таблицу
inset_table_query='''INSERT INTO Students VALUES
                              (201, "Иван", 1),
                              (202, "Петр", 2),
                              (203, "Анастасия", 3),
                              (204, "Игорь", 4);
                              '''

try:
  cursor.execute(inset_table_query)
except sqlite3.Error as error:
     print("Ошибка при работе с SQLite:", error)




def get_student_by_id(student_id):
  select_student_query = f'''SELECT Student_Name, School_Id FROM Students WHERE Student_Id = {student_id};'''

  try:
    cursor.execute(select_student_query)
    records = cursor.fetchall()
  except sqlite3.Error as error:
    print("Ошибка при работе с SQLite:", error)
  
  student_name = records[0][0]
  school_id = records[0][1]
  select_school_query = f'''SELECT School_Name From School WHERE School_Id = {school_id}'''

  try:
    cursor.execute(select_school_query)
    records2 = cursor.fetchall()  
  except sqlite3.Error as error:
    print("Ошибка при работе с SQLite:", error)
  
  school_name = records2[0][0]

  result = f'ID Студента: {student_id}\n Имя студента: {student_name}\n ID школы: {school_id}\n Название школы: {school_name}'
  print(result)


get_student_by_id(202)

cursor.close()
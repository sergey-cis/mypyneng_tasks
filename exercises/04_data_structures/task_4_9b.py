# -*- coding: utf-8 -*-
"""
Завдання 4.9b

У завданні створено список words
words = [
    'Guido', 'van', 'Rossum', 'began', 'working', 'on',
    'Python', 'in', 'the', 'late', '1980s',
]

Треба вивести кожне слово зі списку words на окремому рядку.

Приклад роботи завдання:
$ python task_4_9b.py
Guido
van
Rossum
began
working
on
Python
in
the
late
1980s

Обмеження: не можна редагувати список words.
Буд
е плюсом вирішити завдання без використання циклу for.
"""
words = [
    'Guido', 'van', 'Rossum', 'began', 'working', 'on',
    'Python', 'in', 'the', 'late', '1980s',
]

"""
#My solution
n = str(words).strip("[]").replace("',", "\n").replace("'", "")
print(n)
 """
 #Right solution
result = "\n".join(words)
print(result)



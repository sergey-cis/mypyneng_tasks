"""
Запросити у користувача введення індексу (числа) через input. Якщо за введеним
індексом можна вивести слово зі списку words, вивести його. Якщо індекс більший
за допустимий, вивести повідомлення "У списку words немає такого індексу".


Приклад роботи завдання
$ python task_07.py
Введіть індекс: 0
word1

$ python task_07.py
Введіть індекс: 2
word3

$ python task_07.py
Введіть індекс: 5
У списку words немає такого індексу

Завдання можна ускладнити, додавши підтримку негативних індексів:

$ python task_07.py
Введіть індекс: -1
word3

$ python task_07.py
Введіть індекс: -3
word1

$ python task_07.py
Введіть індекс: -4
У списку words немає такого індексу
"""
words = ["word1", "word2", "word3"]

user_index = int(input("Please enter the index: "))
if user_index < len(words):
    print(words[user_index])
else:
    print("wrong index. try again")
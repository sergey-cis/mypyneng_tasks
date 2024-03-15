# -*- coding: utf-8 -*-
"""
Завдання 6.3

Список data містить різні дані.
data = ["a", "100", "30", 10.5, 20, "test", "15", 100]

Треба відібрати з них лише ті, які вдасться перетворити в integer з допомогою
int. Написати код, який відбирає ті елементи зі списку data, які можна
перетворити на тип integer за допомогою int, робить це перетворення і додає
елементи до нового списку result. У результаті має бути такий список:
[100, 30, 10, 20, 15, 100]

Список data не можна змінювати вручну, всі зміни потрібно зробити за допомогою Python.
"""

data = ["a", "100", "30", 10.5, 20, "test", "15", 100]

# Solution with for-loop

"""
result = []

for symb in data:
    if str(symb).isdigit():
        result.append(int(symb))
print(result)
"""
# Solution with try-except block:
result = []

for vlan in data:
    try:
        new_vl = int(vlan)
    except ValueError:
        pass
    else:
        result.append(new_vl)

print(result)

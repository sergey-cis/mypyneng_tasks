# -*- coding: utf-8 -*-
"""
Завдання 4.6

Обробити рядок ospf_route та вивести інформацію на стандартний потік виведення у вигляді:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для цього використовувати шаблон template і підставити значення з рядка
ospf_route. Значення рядка ospf_route треба отримати за допомогою Python.

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
"""
result = ospf_route.lstrip().replace("[", "").replace("]","").replace("via", " ").replace("," ," ").split()
print(result)
"""

template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""
result = ("".join(ospf_route.strip().replace(",","").replace("via","").replace("[", "").replace("]",""))).split()
print(template.format(result[0],result[1],result[2],result[3],result[4]))
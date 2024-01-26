# -*- coding: utf-8 -*-
"""
Завдання 5.3a

Переробити скрипт із завдання 5.3 таким чином, щоб, крім імені пристрою,
запитувався також параметр пристрою, який потрібно відобразити.

Вивести інформацію про відповідний параметр, зазначеного пристрою.

Приклад виконання скрипту:
$ python task_5_3a.py
Enter device name: r1
Enter parameter name: ios
15.4

Обмеження: не можна змінювати словник london_co.

Це завдання можна зробити без використання умови if.

Важливий момент: для того щоб тест пройшов, текст запиту треба писати саме в
input, а не в print. Тобто так:
device = input("Enter device name: ")

а не так:
print("Enter device name: ")
device = input()
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

dev_name = (input("please enter device name: ")).lower()

dev_param = (input('please enter parameter of the device("ios", "model", "vlans" and so on... ) ')).lower()

if dev_name in london_co.keys():
    for key, values in london_co.items():
        if dev_name == key and (dev_param in london_co[key]):
            #print(london_co[key])
            print(london_co[key][dev_param])
        else:
            print("the device hasn't this parameter")
else:
    print('you enter wrong device name. Try "r1", "r2" or "sw1"')
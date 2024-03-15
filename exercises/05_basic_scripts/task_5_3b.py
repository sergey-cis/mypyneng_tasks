# -*- coding: utf-8 -*-
"""
Завдання 5.3b

Переробити скрипт із завдання 5.3a таким чином, щоб при запиті параметра
відображалися доступні параметри. Параметри треба отримати зі словника, не
прописувати вручну.

Вивести інформацію про відповідний параметр, зазначеного пристрою.

Приклад виконання скрипту:
$ python task_5_3b.py
Enter device name: r1
Enter parameter name (location, vendor, model, ios, ip): ip
10.255.0.1

$ python task_5_3b.py
Enter device name: sw1
Enter parameter name (location, vendor, model, ios, ip, vlans, routing): ip
10.255.0.101

Обмеження: не можна змінювати словник london_co.

Це завдання можна зробити без використання умов if.

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

# My Solution without "if"
user_request = input("Please enter device name: ")
dev_keys  = (london_co.get(user_request)).keys()
ask_param = input("Please enter required parameter from the list: {} ".format(tuple(dev_keys)))
print(london_co[user_request][ask_param])



# My Second solution
#user_request = input('Enter device name: ')
#req_val = []
#for london_co_key, london_co_value in london_co.items():
#    if user_request == london_co_key:
#        for u_k in london_co_value:
#            req_val.append(u_k)
#
#param_request = input('Enter parameter name from the list - {}: '.format(
#    tuple(req_val)))
#print(london_co[user_request][param_request])


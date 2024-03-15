# -*- coding: utf-8 -*-
"""
Завдання 6.6a

Зробити копію скрипта завдання 6.6.

Додати перевірку введеної IP-адреси.
Адреса вважається коректно заданою, якщо вона:
- складається з 4 чисел (а не літер чи інших символів)
- числа розділені точкою
- кожне число в діапазоні від 0 до 255

Якщо адреса неправильна, виводьте повідомлення: "Wrong IP address".  Якщо
адреса правильна, перевіряти та виводити тип адреси як у завданні 6.6.

Повідомлення "Wrong IP address" має виводитися лише один раз, навіть якщо
кілька пунктів вище не виконано.


Приклад виконання скрипту:
$ python task_6_6a.py
Enter IP address: 10.10.1.1
unicast

$ python task_6_6a.py
Enter IP address: 10.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: a.a.10.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.a.a
Wrong IP address

$ python task_6_6a.py
Enter IP address: 10,1,1,1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 500.1.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.1.1.1
Wrong IP address

"""

ip_address = input("Enter IP address: ")
ip_splited = ip_address.split(".")
try:
    oct1,oct2,oct3,oct4 = ip_splited
except (ValueError):
    print("Wrong IP address ")
else:
    try:
        int(oct1),int(oct2), int(oct3),int(oct4) == ip_splited
    except(ValueError):
        print("Wrong IP address") 
    else:
        if 0 <= (int(oct1) or int(oct2) or int(oct3) or int(oct4)) <= 255:
            if 1 <= int(ip_splited[0]) < 224:   
                print("unicast")
            elif 224 <= int(ip_splited[0]) <= 239:
                print("multicast")
            elif oct1 =="0" and oct2 == "0" and oct3 == "0" and  oct4 == "0":
                print("unassigned")
            elif int(oct1) == 255 and int(oct2) == 255 and int(oct3) == 255 and int(oct4) == 255:
                print("local broadcast")
            else:
                print("unused")
        else:
            print("Wrong IP address")
# -*- coding: utf-8 -*-
"""
Завдання 6.6b

Зробити копію скрипта завдання 6.6a.
Доповнити скрипт: якщо адреса була введена неправильно, запитати адресу знову.

Якщо адреса неправильна, виводьте повідомлення: 'Wrong IP address'.
Повідомлення "Wrong IP address" має виводитися лише один раз після кожного
введення адреси, навіть якщо кілька пунктів перевірки адреси не виконано
(приклад виведення нижче).

Приклад виконання скрипту:
$ python task_6_6b.py
Enter IP address: 10.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: a.a.a
Wrong IP address
Enter IP address: 10.1.1.1.1
Wrong IP address
Enter IP address: 500.1.1.1
Wrong IP address
Enter IP address: a.1.1.1
Wrong IP address
Enter IP address: 50.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: 10.a.1.1.1
Wrong IP address
Enter IP address: 255.255.255.255
local broadcast

"""
ip_address = input("Enter IP address: ").strip()


correct_ip = True

while correct_ip:
    ip_splited = ip_address.split(".")
    try:
        oct1,oct2,oct3,oct4 = ip_splited
    except (ValueError):
        print("wrong IP address")
        correct_ip = True
        ip_address = input("Enter IP address: ").strip()
    else:
        try:
            int(oct1),int(oct2), int(oct3),int(oct4) == ip_splited
        except(ValueError):
            print("wrong IP address") 
            correct_ip = True
            ip_address = input("Enter IP address: ").strip()
        else:
            if 0 <= (int(oct1) or int(oct2) or int(oct3) or int(oct4)) <= 255:
                if int(ip_splited[0]) in range(1,224):   
                    print("unicast")
                    correct_ip = False
                elif int(ip_splited[0]) in range(224,240):
                    print("multicast")
                    correct_ip = False
                elif oct1 =="0" and oct2 == "0" and oct3 == "0" and  oct4 == "0":
                    print("unassigned")
                    correct_ip = False
                elif int(oct1) == 255 and int(oct2) == 255 and int(oct3) == 255 and int(oct4) == 255:
                    print("local broadcast")
                    correct_ip = False 
                else:
                    correct_ip = False
                    print("unused")
            else:
                correct_ip = True
                print("wrong IP address")
                ip_address = input("Enter IP address: ").strip()   
            
    
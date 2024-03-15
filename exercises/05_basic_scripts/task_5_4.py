# -*- coding: utf-8 -*-
"""
Завдання 5.4

Запросити користувача введення IP-адреси у форматі: 10.1.1.1

Потім вивести інформацію про адресу у такому форматі:
10        1         1         1
00001010  00000001  00000001  00000001

Перевірити роботу скрипта на різних IP-адресах, наприклад: 192.168.100.1, 10.5.5.190.

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

"""
# My not elegant solution
#user_ip = input('Enter the IP: ')
#ip_list = user_ip.split(".")
#template = """
#          {:<8}  {:<8}  {:<8}  {:<8}
#          {:0>8b}  {:0>8b}  {:0>8b}  {:0>8b}
#      """
#oct1, oct2, oct3, oct4 = ip_list
#num_oct1, num_oct2,num_oct3,num_oct4 = int(oct1), int(oct2), int(oct3), int(oct4)
#
#print(template.format(oct1,oct2,oct3,oct4, num_oct1,num_oct2, num_oct3, num_oct4))


#Right solution from answer
network = input("Enter IP address: ")

ip_list = network.split(".")

oct1, oct2, oct3, oct4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]

ip_output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

print(ip_output.format(oct1, oct2, oct3, oct4))
# -*- coding: utf-8 -*-
"""
Завдання 4.7

Перетворити MAC-адресу в рядку mac на двійковий рядок такого виду:
'101010101010101010111011101110111100110011001100'

Отриманий новий рядок вивести стандартний потік виведення (stdout) за допомогою
print.

Підказка: MAC-адреса без: це шістнадцяткове число AAAABBBBCCCC.

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""

mac = "AAAA:BBBB:CCCC"
"""
new_mac = (" ").join(mac.replace(":", "")).split()

My solution
print("{:^08b}{:^08b}{:^08b}{:^08b}{:^08b}{:^08b}{:^08b}{:^08b}{:^08b}{:^08b}{:^08b}{:^08b}".format(int(new_mac[0], 16),
                                        int(new_mac[1], 16),int(new_mac[2], 16), int(new_mac[3], 16), int(new_mac[4], 16),
                                        int(new_mac[5], 16), int(new_mac[6], 16), int(new_mac[7], 16), int(new_mac[8], 16),
                                        int(new_mac[9], 16), int(new_mac[10], 16), int(new_mac[11],16)))
                                        """

#"Right solution"
result = int(mac.replace(":", ""), 16)
print("{:b}".format(result))
'''
Задание 1.
Условие:
Написать функцию на Python, которой передаются 
в качестве параметров команда и текст. 
Функция должна возвращать True, если команда успешно 
выполнена и текст найден в её выводе и False в противном случае. 
Передаваться должна только одна строка, разбиение вывода использовать не нужно.

Задание 2. (повышенной сложности)
Доработать функцию из предыдущего задания таким образом, 
чтобы у неё появился дополнительный режим работы, в котором 
вывод разбивается на слова с удалением всех знаков пунктуации 
(их можно взять из списка string.punctuation модуля string). 
В этом режиме должно проверяться наличие слова в выводе.
'''
import subprocess

def out_command_text() -> bool:
    out = result.stdout
    with open('text.txt', 'w', encoding='utf-8') as file:
        file.write(out)
        if '21.2' in out and 'Green Linux' in out:
                return True
        else:
                return False
        
result = subprocess.run('cat /etc/os-release', shell = True, stdout = subprocess.PIPE, encoding = 'utf-8')

if __name__=='__main__':
    print(out_command_text())

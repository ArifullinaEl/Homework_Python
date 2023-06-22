# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной 
# Задача 38: Дополнить телефонный справочник 
# возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения
# и удаления данных

def write_contact(filename):
    with open(filename, 'a', encoding = 'utf-8') as file:
        file.write('\n' + input(f'Введите данные через пробел '))
        return file
    
def read_contact(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        for line in file:
            print(line.strip())
        return file
    
    # contacts = []
    # with open(filename, 'r', encoding = 'utf-8') as file:
    #     for line in file:
    #         n, surn, fam, ph = line.strip().split(' ')
    #         contact = {
    #             'name': n,
    #             'surname': surn,
    #             'family': fam,
    #             'phone': ph
    #         }
    #         print(n, surn, fam, ph)
    #         contacts.append(contact)
    # return contacts

# def change_contact(filename):
    
def change_contact(filename):
    contacts = []
    with open(filename, 'r', encoding = 'utf-8') as file:
        for line in file:
            contacts.append(line.strip())
        print(contacts)
        
    ch = input('Кого будем менять? ')
    
    for i in range(len(contacts)):
        if ch in contacts[i]:
            new = input('Введите изменения: ')
            contacts[i] = new
    
    with open(filename, 'w', encoding = 'utf-8') as file:
        for i in contacts[:-1]:
            file.write(i + '\n')
        file.write(contacts[-1])


def search_contact(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        s = input('Введите что ищем? ')
        for line in file:
            if s in line:
                print(line.strip())
            # else:
            #     print('Не найдено') 
        return file


f = r'HW 18_06_2023\book.txt'
print('1 - ввод/добавление данных\n2 - печать данных\n3 - изменение/удаление данных\n4 - поиск данных')
a = int(input('Введите цель: '))

if a == 1:
    a_cont = write_contact(f)
elif a == 2:
    r_cont = read_contact(f)
elif a == 3:
    ch_cont = change_contact(f)
elif a == 4:
    s_cont = search_contact(f)
else:
    print('Вы ошиблись, попробуйте снова')

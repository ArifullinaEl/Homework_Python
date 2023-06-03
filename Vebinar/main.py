# a = [0, 1, 2, 2, 3, 4]
# print(len(set(a)))

# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# a = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(a)))


# a = [1, 2, 3, 4, 5]
# k = 3

# for i in range(k):
#     a.insert(0, a.pop(-1))
# print(a)





# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3

# Output:  [3, 4, 5, 1, 2]

# a = [1, 2, 3, 4, 5]
# k = 3

# lst = [1, 2, 3, 4, 5]
# k = 3
# lst = lst[-k:] + lst[:-k]
# print(lst)

# # print(list_1.insert(х, y)) - первое число позиция элемента, а второе число это какое число нужно вставить

# lst = [1, 2, 3, 4, 5]
# k = 3

# for i in range(k):
#     num = lst.pop(-1)
#     lst.insert(0, num)

# print(lst)

# shop_dict = {
#     0: {
#         'name': 'стул',
#         'кол-во': 3
#     },
#     5: {
#         'name': 'стол',
#         'кол-во': 7
#     },
#     8: {
#         'name': 'диван',
#         'кол-во': 10
#     }
# }

# print(shop_dict[5]['name'])

# start_lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

# val_list = []
# for little_dict in start_lst:
#     for val in little_dict.values():
#         val_list.append(val)
# print(set(val_list))


# https://t.me/GPT_chat_robot


# 

# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that 
# she sells are sea shells I'm sure So if she sells sea shells 
# on the sea shore I'm sure that the shells are sea shore shells

# Output: 13


# input_str = ("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".upper()).split()
# arr = set(input_str)
# print(len(arr))


# arr = """She sells sea shells on the sea shore The shells 
# that she sells are sea shells I'm sure So if she sells sea 
# shells on the sea shore I'm sure that the shells are sea shore shells""".lower().split(" ")
# print(len(set(arr)))


# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
#     “Задана последовательность неотрицательных целых чисел.
#     Требуется определить значение наибольшего элемента
#     последовательности, которая завершается первым
#     встретившимся нулем (число 0 не входит в последовательность)”.
#     Однако 2  друга оказались не такими смышлеными. Никто 
#     из ребят не смог до конца сделать это задание. Они 
#     решили так: у кого будет меньше ошибок в коде, тот и 
#     выиграл спор. За помощью товарищи обратились к Вам, студентам.


# chislo = 0
# while True:
#     num = int(input())
#     if num > 0:
#         if chislo < num:
#             chislo = num
#     else:
#         break

# print(chislo)



# maxx = -1

# while (num:=int(input('--> '))) != 0:
#     if num > maxx:
#         maxx = num

# print(maxx)


# def fib(n):
#     if n in (0, 1):
#         return 1
#     return fib(n-1) + fib (n-2)


# m = int(input('Введите n: '))
# print(fib(m))



# n = int(input('Vvedite chislo N: '))

# def fib(n):
#     if n in[1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
    
# print(fib(n))


# def fib(n):
#     if n == 0:
#         return 0
#     elif n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)


# def fib(n):
#     if n == 0:
#         return 0
#     elif n in [1, 2]:
#         return 1
#     return fib(n - 2) + fib(n - 1)


# n = int(input('Vvedite chislo N: '))
# print(fib(n))


# Хакер Василий получил доступ к классному журналу 
# и хочет заменить все свои минимальные оценки на 
# максимальные. Напишите программу, которая заменяет 
# оценки Василия, но наоборот: все максимальные – 
# на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1


# import random

# def create_journal(n):
#     journal_=[]
#     for i in range(n):
#         journal_.append(random.randint(1,5))
#     return journal_

# def change_min_max(number_list):
#     min_number = min(number_list)
#     max_number = max(number_list)
#     for i in range(len(number_list)):
#         if number_list[i] == max_number:
#             number_list[i] = min_number
#     return number_list

# n = int(input('Введите количество оценок в классном журнале Василия: '))
# test_list = create_journal(n)
# print(test_list)
# test_list = change_min_max(test_list)
# print(test_list)

# ocenki=[1,4,3,3,4]
# min_= min(ocenki)
# max_= max(ocenki)
# for i in range(len(ocenki)):
#     if ocenki[i] == max_:
#         ocenki[i]=min_
#     for i in ocenki]
# print(ocenki)



# def simple_num(num):
#     for i in range(2, num - 1):
#         if num%i == 0:
#             return 'No'
#     return 'Yes'
    
    
# print(simple_num(1))



# def reverse_input(n):
#     num = input('--> ')
#     if n == 1:
#         return num
#     return reverse_input(n - 1) + ' ' + num


# print(reverse_input(3))
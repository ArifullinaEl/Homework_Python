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
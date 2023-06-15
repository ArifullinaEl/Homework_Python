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

# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# arr_one = []
# n = int(input('Введите размер первого массива: '))
# for i in range(n):
#     a = int(input(f"Введите {i+1}-й элемент: "))
#     arr_one.append(a)
  
# arr_two = []
# m = int(input('Введите размер второго массива: '))
# for j in range(m):
#     a = int(input(f"Введите {j+1}-й элемент: "))
#     arr_two.append(a) 
    
# arr_result = []   
    
# print(f"Первый массив: {arr_one}")
# print(f"Второй массив: {arr_two}")  

# for i in range(n):
#     if arr_one[i] not in arr_two:
#         arr_result.append(arr_one[i]) 
        
# print(arr_result) 


# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 
# 1 5 1 5 1
# Вывод: Вывод:
# 0 2

# arr_one = []
# n = int(input('Введите размер первого массива: '))
# for i in range(n):
#     a = int(input(f"Введите {i+1}-й элемент: "))
#     arr_one.append(a)
   
# print(f"Первый массив: {arr_one}")

# count = 0
# for i in range(1, n-1):
#     if arr_one[i] > arr_one[i-1] and arr_one[i] > arr_one[i+1]:
#         count +=1
        
# print(count) 

# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 
# Вывод:
# 1 2 3 2 3
# 2

# arr_one = []
# n = int(input('Введите размер первого массива: '))
# for i in range(n):
#     a = int(input(f"Введите {i+1}-й элемент: "))
#     arr_one.append(a)
   
# print(f"Первый массив: {arr_one}")

# count = 0
# for i in range(n):
#     for j in range(i+1, n):
#             if arr_one[i] == arr_one[j]:
#                 count +=1
        
# print(count)

# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284


# В списке хранятся числа. Нужно выбрать только чётные числа
# и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# nums = [1, 2, 3, 5, 8, 15, 23, 38]
# result_arr = []
# for i in range(len(nums)):
#     if nums[i]%2 == 0:
#        result_arr.append((nums[i], nums[i]**2)) 
       
# print(result_arr)

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res) 

# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# print(transormed_values == values)


# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(lambda x: x, values))
# print(transormed_values == values)

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# def find_farthest_orbit(orbits):
#     s = [(a[0]*a[1] if a[0]!=a[1] else 0) for a in orbits]
#     return orbits[s.index(max(s))]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))


# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: 
# Вывод:
# values = [0, 2, 10, 6]
# same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by(func, vals):
    return len(set(map(func, vals))) in [0, 1]

values = [0, 2, 10, 7]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
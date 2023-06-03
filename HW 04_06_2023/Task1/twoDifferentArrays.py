# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого 
# множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.


arr_one = []
n = int(input('Введите размер первого массива: '))
for i in range(n):
    a = int(input(f"Введите {i+1}-й элемент: "))
    arr_one.append(a)



arr_two = []
m = int(input('Введите размер второго массива: '))
for j in range(m):
    a = int(input(f"Введите {j+1}-й элемент: "))
    arr_two.append(a)    
    
print(f"Первый массив: {arr_one}")
print(f"Второй массив: {arr_two}")


arrset_one = set(arr_one)
print(arrset_one)

arrset_two = set(arr_two)
print(arrset_two)

u = arrset_one.union(arrset_two)
print(u)

res = []
for k in u:
    res.append(k)
    
print(res)

   
print(sorted(res))



 
        
    



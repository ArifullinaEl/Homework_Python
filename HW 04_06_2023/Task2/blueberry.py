# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке 
# растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора 
# черники. Эта система состоит из управляющего модуля и нескольких 
# собирающих модулей. Собирающий модуль за один заход, находясь 
# непосредственно перед некоторым кустом, собирает ягоды с этого
# куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.


import random
arr = []

n = int(input('Введите количество кустов черники: '))

for i in range(n):
    arr.append(random.randint(1,10))
    
print(arr)
    
res_arr = []
for i in range (n-1):
    res_arr.append(arr[i-1] + arr[i] + arr[i+1])


res_arr.append(arr[-2] + arr[-1] + arr[0])

print(max(res_arr))
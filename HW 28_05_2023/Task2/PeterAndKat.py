'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет 
сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)'''


s = int (input('Введите сумму чисел: '))
p = int (input('Введите произведение чисел: '))

d = round ((s * s) - (4 * p))

x = round (s + d ** (0.5))/2
y = round (s - d ** (0.5))/2

print (f"Первое загаданное число {x}")
print (f"Второе загаданное число {y}")


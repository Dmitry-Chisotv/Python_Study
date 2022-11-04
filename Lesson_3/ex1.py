# Задача 3-1. 
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
n=int(input('Введите число n, для списка из n чисел: '))
list1=[]
for i in range(n):
    list1.append(random.randint(1, 99))
print (list1)

sum = 0
for i in range (len(list1)):    
    if i % 2 !=0:
        print (list1[i])
        sum = sum + int(list1[i])
        
print (sum)



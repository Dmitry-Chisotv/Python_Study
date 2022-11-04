# Задача 3-2.  Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


import random
n=int(input('Введите число n, для списка из n чисел: '))
list1=[]
for i in range(n):
    list1.append(random.randint(1, 5))
print (list1)

prod = 1
for i in range(len(list1)):
    if i >= n/2:
        prod=list1[i]*list1[n-(1+i)]
        print (prod)    





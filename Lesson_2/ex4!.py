# Задача 2-4. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# !!!Позиции хранятся в файле file.txt в одной строке одно число.

import random
N=int(input('Введите число N: '))
prod =1 

list1=[]
for i in range(N):
    list1.append(random.randint(-N, N))
    prod = prod * int(list1[i])
print (list1)
print (prod)

#   Файл не удается считать 
# 
#        
# file=open('file.txt', 'r')
# a=[]
# prod =1

# print ('В файле: ')    
# for i in file:
#     a.append(int(i))
#     # print (i, end='')
# a=set(a)

# for i in a:
#     if int(i) < len (list1):
#         prod = prod * list1[int(i)]
# file.close()
        
# print (prod)







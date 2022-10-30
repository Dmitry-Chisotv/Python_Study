# Задача 2-5. Реализуйте алгоритм перемешивания списка.

import random

N=int(input('Введите число N: '))
temp = 0
list1=[]
for i in range(N):
    list1.append(random.randint(1, 100))
print (list1)

for i in range(len(list1)):
    if i >= N/2:
        temp=list1[i]
        list1[i]=list1[N-(1+i)]
        list1[N-(1+i)]=temp
print (list1)

# if i > N/2:
#     temp=list1[i]
#     list1[i]=list1[N-(1+i)]
#     list1[N-(1+i)]=temp
#     i+=1
# print (list1)
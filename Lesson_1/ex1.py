# Задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет


n=int(input('Введите цифру от 1 до 7 соответствующую дню недели: '))
if n >0 and n<8:
    if n < 6 :
        print (f"{n} будний день")
    else:
        print (f"{n} выходной день")
else:
  print (f"{n} некорректная цифра, не соотвествующая дню недели")  



# Задача 2-1. Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n=input('Введите число, сумму цифр которого определяем: ')
sum = 0

n1=n.replace('.', '')

#print(n1)

for i in range(len(n1)):
    sum = sum + int(n1[i])
    
print(sum)




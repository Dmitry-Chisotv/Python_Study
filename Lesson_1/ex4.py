# Задача 4. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве.
#Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


xa=int(input('Введите значение координаты Х для точки А: '))
ya=int(input('Введите значение координаты Y для точки А: '))

xb=int(input('Введите значение координаты Х для точки B: '))
yb=int(input('Введите значение координаты Y для точки B: '))

d= ((xb-xa) **2 + (yb-ya) **2) **0.5
print (f"Расстояние между точками {d}")


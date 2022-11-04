# Задача 3-5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 



N=int(input('Введите число N: '))


fib1=0
fib2=1

print (fib1)
print (fib2)

i=0
while i < N - 2:
    fib_sum=fib2+fib1
    fib1=fib2
    fib2=fib_sum
    i=i+1
    print (fib2)


fib1=-1
fib2=1

print (fib1)
print (fib2)

i=0
while i < N-2:
    fib_sum=fib1-fib2
    fib1=fib2
    fib2=fib_sum
    i=i+1
    print (-fib2)

# Фибоначчи рекурсией:

# def fib (N):
#     if N <=2:
#         return 1
#     else:
#         return fib(N-1)+fib(N-2)
# list=[]
# for e in range (1, N+1):
#     list.append(fib(e))
# print (list)
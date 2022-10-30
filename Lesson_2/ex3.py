# Задача 2-3. 
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ ((1+1/n)**n)
# и выведите на экран их сумму.
# Пример: Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} 
# Сумма 9.06

n=int(input('Введите число n, для списка из n чисел последовательности ((1+1/n)**n): '))
sum = 0
list1=[]

for i in range(n+1):
    list1.append(int(i))
    print (list1[i])

for i in range(len(list1)):
    if i!=0:
        list1[i]=((1+1/i)**i)
        print (round(list1[i], 2))
        sum += list1[i]
   
print (round(sum, 2))

# Задача 5-1. 
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст через пробел:\n")
print(f"Исходный текст: {text}")
find_text = "абв"
lst = [i for i in text.split() if find_text not in i]
print(f'Результат: {" ".join(lst)}')
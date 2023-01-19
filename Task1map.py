# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
unique_list = [i for i in set(lst) if lst.count(i) == 1]
print(f"Неповторяющиеся элементы {unique_list}")
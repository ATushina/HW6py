# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import *
nums = [randint(1, 10) for i in range(16)]
print("Список: ", nums, '\n')
nums = list(filter(lambda x: nums.count(x) == 1, nums))  
print("Уникальные элементы: ", nums)
nums = list(enumerate (nums))
print("Уникальные элементы:", nums)
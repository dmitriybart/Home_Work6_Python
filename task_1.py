# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

num = [2, 3, 5, 258, 3]
sum = 0
l = [i for i in range(len(num))]
post = list(filter((lambda x:  x%2!=0), l))
for i in post:
        sum += num[i]
print(sum)
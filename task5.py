# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

A = [int(input('введите х1: ')), int(input('введите у1: '))]
B = [int(input('введите х2: ')), int(input('введите у2: '))]
print(round(pow((A[0]-B[0])**2+(A[1]-B[1])**2, 0.5), 3))

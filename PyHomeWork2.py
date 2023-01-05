# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input('Введите вещественное число: ')
# i = 0
# sum = 0
# for i in range(len(number)):
#     if number[i]!= ',' and number[i]!= ".":
#         t = int(number[i])
#         sum = sum + t
# print(sum)

#-------------------------------------------------------------------------------------------------

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите целое число: '))
# mult = 1
# i = 1
# result = ''
# while i <= number:
#     mult *=  i
#     if i == number:
#         result = result + str(mult)
#     else:
#         result = result + str(mult) + ', '
#     i +=1
# print(result)


#-------------------------------------------------------------------------------------------------

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

# number = int(input('Введите целое число: '))
# i = 1
# result = {}
# while i<=number:
#     f = (1+1/i)**i
#     result[i]=round(f, 2)
#     i += 1
# i = 1
# sum = 0
# while i<=number:
#     sum += result[i]
#     i += 1
# print(result)
# print(sum)

#-------------------------------------------------------------------------------------------------

#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# number = int(input('Введите целое число: '))
# list_numbres = [i for i in range(-number,number+1)]
# print(list_numbres)
# result = 1
# file = open('file.txt','r')
# for line in file:
#     print(list_numbres[int(line)])
#     result *= list_numbres[int(line)]
# print(f'Произведение: {result}')

#-------------------------------------------------------------------------------------------------

#Реализуйте алгоритм перемешивания списка.
import datetime

def random(max_number):
    random = datetime.datetime.now().microsecond/10**6
    return random*max_number

list_numbres = [0, 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
print(list_numbres)
for i in range(len(list_numbres)-1,-1,-1):
    j = int(random(i+1))
    list_numbres[i], list_numbres[j] = list_numbres[j], list_numbres[i]
print(list_numbres)
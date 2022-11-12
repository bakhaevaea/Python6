
import random

def NumNum(num, count):
    numCount = ""
    for i in range(count):
        numCount += num 
    return numCount

def TaskHome1():
#     Задача 1. Дано натуральное число N. Найдите значение
#       выражения:
#       N + NN + NNN
#       N может быть любой длины.
    number = input("Введите натуральное число  ")
    print(f"{number} + {NumNum(number, 2)} + {NumNum(number, 3)} = {str( int(number) + int(NumNum(number,2)) + int(NumNum(number, 3) ) ) }")


def TaskHome2():
    # Задача 2. Задан массив из случайных цифр на 15 элементов.
    # На вход подаётся трёхзначное натуральное число. Напишите
    # программу, которая определяет, есть в массиве
    # последовательность из трёх элементов, совпадающая с
    # введённым числом.
    numbers = [random.randint(0,9) for i in range(15) ]
    print(numbers)
    num = input("Введите трехзначное число  ")
    numbersStr = ""
    for i in numbers:
        numbersStr += str(i)  
    print("Последовательность есть" if numbersStr.count(num) > 0 else "Такой последовательности нет")


def Prost(num1, num2):
    # преверяем не сократимая ли дробь
    nesokr = True
    for i in range(2, num1+1):
        if num1 % i == 0 and num2 % i == 0:
            return False
    return nesokr
     

def TaskHome3():
    # Задача 3. Найдите все простые несократимые дроби,
    # лежащие между 0 и 1, знаменатель которых не превышает 11.
    print("Простые несократимые дроби между 0 и 1:")
    for i in range(2,12):
        for j in range(1,i+1):
            if Prost(j, i):
                print(f"{j}/{i}, ", end = " ")
    
    
 
# TaskHome1()
# TaskHome2()
TaskHome3()
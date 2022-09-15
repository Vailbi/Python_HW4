# №1 Вычислить число c заданной точностью d

# accuracy = len(input()) - 2
# num = round(float(input()), 5)
#
#
# def toFixed(inp, accur=0):
#     return f"{inp:.{accur}f}"
#
#
# print(toFixed(num, accuracy))


# №2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# number = int(input())
# result = []
# div = 2
# while div <= number:
#     if number % div == 0:
#         result.append(div)
#         number /= div
#     else:
#         div += 1
# print(set(result))


# №3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.

# inputArr = map(int, input("Введите числа через пробел: ").split())
# print(set(inputArr)


# №4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# import random
#
# k = int(input("Введите коэффициент К: "))
#
# def creat_file(st):
#     with open('result.txt', 'w') as data:
#         data.write(st)
#
def rnd():
    return random.randint(1, 25)

def crtng_an_equation(j):
    if j>1:
        return f"{rnd()}x^{j}"
    elif j == 1:
        return f"{rnd()}x"

def summa_eqation(x):
    result = ""
    if k ==0:
        print("Коэффицент не может быть равен 0!")
        exit()
    while x >=1:
        result+= f"{crtng_an_equation(x)}+"
        x-=1
    else:
        result += f"{rnd()}"
    return result

# print(summa_eqation(k))
creat_file(summa_eqation(k))



# №5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.


import sympy


def read_file(f):
    res = open(f, 'r')
    text = res.readline()
    res.close()
    return text


formula1 = read_file("formula.txt")  # 11*x**3 + 2*x**2 + 24*x + 16
formula2 = read_file("formula2.txt")  # 3*x**2 + 15*x -4

summa = formula1 + "+" + formula2

result = str(sympy.simplify(summa))

print(result)


def prnt_res(arr):  # вывод результата в читабельном виде
    arr = arr.replace('**', '^')
    arr = arr.replace('*', '')
    return arr

def creat_file(st):
    with open('result2.txt', 'w') as data:
        data.write(st)


print(prnt_res(result))
creat_file(prnt_res(result))

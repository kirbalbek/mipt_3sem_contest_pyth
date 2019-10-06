'''
Представьте натуральное число n в виде суммы двух кубов неотрицательных целых чисел. Т.е. n = a^3 + b^3, где n - натуральное, a и b - неотрицательные целые. Если такое представление возможно, выпишите найденные числа a и b через пробел в порядке неубывания. Если разложить нельзя, напишите строку "impossible".
Формат входных данных

Натуральное число.
Формат выходных данных

Если представление возможно, два числа через пробел в порядке неубывания, в противном случае строка "impossible".
'''
n = int(input())
ab_exist = False
addend_max = round(n**(1/3))
for a in range (addend_max+1):
    for b in range (a, addend_max+1):
        if a ** 3 + b ** 3 == n:
            print(a, b)
            ab_exist = True
if ab_exist is False:
    print("impossible")
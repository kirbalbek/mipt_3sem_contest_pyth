'''
Вам необходимо написать программу, вычисляющую минимальное число, для которого заданы: 1) сумма цифр, 2) количество цифр, 3) цифры должны быть упорядочены по неубыванию.
Формат входных данных

Сумма и количество цифр через пробел.
Формат выходных данных

Число-ответ или строка 'impossible', если такого числа не существует.
'''
summa, amount = map(int, input().split())
chislo = [int(1)]*amount
numb_exist = False

for i in range(amount-1, -1, -1):
    for j in range(1, 10):
        chislo[i] = j
        if sum(chislo) == summa:
            print(''.join(map(str, chislo)))
            numb_exist = True
if numb_exist is False:
    print("impossible")

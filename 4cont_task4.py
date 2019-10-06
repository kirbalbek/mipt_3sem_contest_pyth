'''
Необходимо написать функцию prime(n), генерирующую n-ое простое число, где n - натуральное. Первым простым числом является 2, вторым - 3, третьим - 5 и так далее.
Формат входных данных

Натуральное число - n
Формат выходных данных

n-ое простое число
'''
def prime(n):
    num = int(2)
    ch_max = num
    while n > 0:
        flag = int(1)
        for i in range (2, num//2+1):
            if num%i==0:
                flag = int(0)
        if flag == 1:
            ch_max = num
            n-=1
        num+=1
    return ch_max

inp_num = int(input())
print(prime(inp_num))

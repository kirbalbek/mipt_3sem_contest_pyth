sum_vvod = int(0)
sum_alg = int(0)
N = int(input())
sum_vvod+=N
el_max = N
el_min = N

while N!=0:
    N = int(input())
    sum_vvod+=N
    if el_max < N:
        el_max = N
    elif el_min > N and N!=0:
        el_min = N

for i in range (el_min, el_max+1):
    sum_alg += i

print(sum_alg - sum_vvod)

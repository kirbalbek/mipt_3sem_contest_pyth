amo = int(0)
sum = int(0)
N = int(input())

amo +=1
sum +=N

while N != 0:
    N = int(input())
    sum += N
    amo += 1

amo = amo - 1
if amo == 0:
    print(amo)
else:
    srzn = round(sum/amo, 2)
    print(srzn)

max = int(input())
if max == 0:
    print(max)
else:
    N = int(1)
    while N != 0:
        N = int(input())
        if N != 0 and N > max:
            max = N
    print(max)

q = [1, 0, 0, 0, 0, 0]
Nmax = int(0)

while q[0]!=0:
    if q[5]>Nmax:
        Nmax = q[5]
    q[5] = q[4]
    q[4] = q[3]
    q[3] = q[2]
    q[2] = q[1]
    q[1] = q[0]
    q[0] = int(input())
print(Nmax)    

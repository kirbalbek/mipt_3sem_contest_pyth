N = int(input())
q = [0, 0, 0, 0]
q_num = int(0)
q_max = int(0)

for i in range (N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x > 0 and y > 0:
        q[0] += 1
    elif x > 0 and y < 0:
        q[3] += 1
    elif x < 0 and y > 0:
        q[1] += 1
    elif x < 0 and y < 0:
        q[2] += 1

for j in range(4):
    if q[j] > q_max:
        q_num = j+1
        q_max = q[j]

if q_max == 0:
    q_num+=1
print(q_num, q_max)

N = int(input())
sum = int(0)

for i in range (3):
    sum += N%10
    N = N//10
print(sum)

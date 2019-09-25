count_var = int(0)
count_same = int(0)
n = int(input())
max = False
while n!=0:
    if max is False:
        max = n
    count_var+=1
    if n == max:
        count_same += 1
    if n>max:
        max = n
        count_same = 1
    n = int(input())
print(count_var-count_same)

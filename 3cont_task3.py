n = int(input())
count_var = int(0)
mid_sum = int(0)
squared_mid_sum = int(0)
d = int(0)
while n != 0:
    count_var+=1
    mid_sum+=n
    squared_mid_sum+=n**2
    n = int(input())
mid = round(mid_sum/count_var, 3)
d = round(squared_mid_sum/count_var - (mid_sum/count_var)**2, 3)
print(mid, d)

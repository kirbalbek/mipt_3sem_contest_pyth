num_nega = input()
num_dex = int(0)
nega_pow = len(num_nega)-1
for i in num_nega:
     num_dex += int(i)*(-10)**(nega_pow)
     nega_pow-=1
print(num_dex)

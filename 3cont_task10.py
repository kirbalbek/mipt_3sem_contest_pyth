dex_num = int(input())
bab_num=[]
while dex_num>0:
    place_num=dex_num%60
    place_str="<"*(place_num//10)+"v"*(place_num%10)
    bab_num.append(place_str)
    place_str = str()
    dex_num = dex_num//60
bab_num.reverse()
print('.'.join(bab_num))

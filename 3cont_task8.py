see_count = int(0)
height = int(input())
height_max = height
see_count += 1
while height != 0:
    if height_max < height:
        see_count +=1
        height_max = height
    height = int(input())
print(see_count)        

max1 = False
max2 = False
min1 = False
min2 = False

n = int(input())
for word in input().split():
    word = int(word)

    if max1 is False:
        max1 = word
    elif max1 >= word and max2 is False:
        max2 = word

    if min1 is False:
        min1 = word
    elif min1 <= word and min2 is False:
        min2 = word

    if max1 < word and max1 is not False:
        max2 = max1
        max1 = word
    elif max2 < word and max2 is not False:
        max2 = word

    if min1 > word and min1 is not False:
        min2 = min1
        min1 = word
    elif min2 > word and min2 is not False:
        min2 = word

print(min1+min2, max1+max2)

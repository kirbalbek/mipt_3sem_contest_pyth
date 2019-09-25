a = int(input())
b = int(input())
c = int(input())

if a == 0 or b == 0 or c == 0:
    print ("impossible")
else:
    mas = [a, b, c]
    mas = sorted(mas)
    cosa = (mas[0]**2 + mas[1]**2 - mas[2]**2)/(2*mas[0]*mas[1])

    if mas[2] >= mas[0] + mas[1]:
        print("impossible")

    elif cosa > 0:
        print("acute")
    elif cosa == 0:
        print("right")
    else:
        print("obtuse")
# right, acute, obtuse, impossible

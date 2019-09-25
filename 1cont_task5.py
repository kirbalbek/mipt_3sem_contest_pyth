numb = int(input())
anim = input()
a = int(0)
if anim == "parrot":
    a = numb//10
elif anim == "monkey":
    a = numb//90
elif anim == "elephant":
    a = numb//300
if a == 0:
    a = 1
print(a)

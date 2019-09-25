stri = input()
max_num = 0
num_stri = str()
for i in stri:
    if (i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5"
    or i == "6" or i == "7" or i == "8" or i == "9"):
        num_stri+=i
    elif num_stri == '':
        stri = ''
    else:
        if int(num_stri) > max_num:
            max_num = int(num_stri)
        num_stri=str()
print(max_num)

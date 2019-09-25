speed, lic_plate = input().split()
salary = int(0)
while lic_plate != "A999AA":
    if int(speed) > 60:
        if lic_plate[1] == lic_plate[2] and lic_plate [2] == lic_plate[3]:
            salary += 1000
        elif lic_plate[1] == lic_plate[2] or lic_plate [1] == lic_plate[3]:
            salary += 500
        elif lic_plate[2] == lic_plate[3]:
            salary += 500
        else:
            salary += 100
    speed, lic_plate = input().split()
print(salary)

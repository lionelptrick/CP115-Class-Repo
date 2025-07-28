inputs = input().split()
yardLength = float(input[0])
yardWidth = float(input[1])
houseLength = float(input[2])
houseWidth = float(input[3])
wage = (yardLength * yardWidth - houseLength * houseWidth) * 2
print(wage)

yardLength = float(input())
yardWidth = float(input())
houseLength = float(input())
houseWidth = float(input())
yardArea = yardLength * yardWidth
houseArea = houseLength * houseWidth
totalWage = yardArea - houseArea * 2
print(totalWage)

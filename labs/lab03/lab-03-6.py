yardLength, yardWidth, houseLength, houseWidth = map(float, input().split())
totalWage = yardLength * yardWidth - houseLength * houseWidth * 2
print(totalWage)

score1 = 85
score2 = 92.5
score3 = 78

average = (score1 + score2 + score3) / 3
print(f"Average: {average}")
print(f"Type of Average: {type(average)}")
print()
average_int = int(average)
difference = average - average_int
print(f"Average as integer: {average_int}")
print(f"Difference from the original average: {difference}")
print()
calculation = score1 ** 2 / score2 + score3 % 7
print(f"Calculation result: {calculation}")
print(f"Type of Calculation: {type(calculation)}")

#Explanation:
#int(score2) removes the decimal part, so 92.5 becomes 92
#float(score1) converts an integer into a float representation
print("\n --- Average Score Calculator ---")

print("\nPlease enter your scores:")
scores1 = int(input("Scores 1: "))
scores2 = int(input("Scores 2: "))
scores3 = int(input("Scores 3: "))

total_scores = scores1 + scores2 + scores3
average = total_scores/3

print("\n---- Results ----")
print(f"Scores 1: {scores1}")
print(f"Scores 2: {scores2}")
print(f"Scores 3: {scores3}")
print(f"Total Scores: {total_scores}")
print(f"Average: {average:.2f}")
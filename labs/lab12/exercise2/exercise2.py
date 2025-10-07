score = float(input())

# Initialize variables
total_score = 0
score_count = 0

# Loop until a score outside 0-100 is entered
while 0 <= score <= 100:
    total_score += score
    score_count += 1
    score = float(input())

# Calculate average
if score_count > 0:
    average_score = total_score / score_count
else:
    average_score = 0

print(score_count)
print(total_score)
print(f"{average_score:.2f}")

print("--- Student Grade System ---")

# List of student grades for 5 tests
test1 = 78
test2 = 85
test3 = 92
test4 = 67
test5 = 88

# Calculate total points scored and average score
totalpoints = test1 + test2 + test3 + test4 + test5
average_score = totalpoints / 5

# Calculate percentage each test contributes to the total score
percentage1 = (test1 / totalpoints) * 100
percentage2 = (test2 / totalpoints) * 100
percentage3 = (test3 / totalpoints) * 100
percentage4 = (test4 / totalpoints) * 100
percentage5 = (test5 / totalpoints) * 100

# Display test scores for 5 tests
print("\nTest Scores:")
print(f"Test 1: {test1}")
print(f"Test 2: {test2}")
print(f"Test 3: {test3}")
print(f"Test 4: {test4}")
print(f"Test 5: {test5}")

# Display total points and average score
print(f"\nTotal points {totalpoints} out of 500")
print(f"Average: {average_score}")

# Display percentage contribution of each test
print("\nPercentage Contribution of Each test:")
print(f"Test 1: {percentage1:.2f}")
print(f"Test 2: {percentage2:.2f}")
print(f"Test 3: {percentage3:.2f}")
print(f"Test 4: {percentage4:.2f}")
print(f"Test 5: {percentage5:.2f}")

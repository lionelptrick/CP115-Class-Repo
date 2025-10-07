num_days = int(input())
danger_threshold = float(input())

# TODO: Your code here
# Use input() inside the loop to get each day's temperature
danger_days = 0
total_temp = 0.0

for i in range(num_days):
    temperature = float(input())
    total_temp = total_temp + temperature
    if temperature > danger_threshold:
        danger_days = danger_days + 1

average_temp = total_temp / num_days


print(danger_days)
print(f"{average_temp:.1f}")
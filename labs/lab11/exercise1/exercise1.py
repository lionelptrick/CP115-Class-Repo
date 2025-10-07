
num_rounds = int(input())  

total_score = 0.0
rounds_processed = 0

for i in range(num_rounds):
    round_score = float(input())  
    if round_score > 100:
        round_score += round_score * 0.2  
    total_score += round_score
    rounds_processed += 1

print(f"{total_score:.1f}")
print(rounds_processed)

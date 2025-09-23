day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()

# TODO your code here
if day_type == "Weekend":
    if customer_type == "Adult":
        base_price = 18
    elif customer_type == "Child":
        base_price = 12
    elif customer_type == "Senior":
        base_price = 15
    else:
        base_price = 0
else:
    if customer_type == "Adult":
        base_price = 15
    elif customer_type == "Child":
        base_price = 10
    elif customer_type == "Senior":
        base_price = 12
    else:
        base_price = 0 

final_price = base_price
if show_time > 18:
    final_price += 3

if is_student == "Yes" and day_type == "Weekend":
    final_price *= 0.9

print(base_price)
print(final_price)
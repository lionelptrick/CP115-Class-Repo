# Programmer's Name: LIONEL ANAK PATRICK PAT
# Problem Description: This program calculate a customer's monthly usage and then calculates and displays the amount of the bill to be paid after receiving the discount

# Ask user to enter their monthly usage
monthly_usage = float(input("Enter your monthly usage: RM "))

# Declare discount = 0 by default
discount = 0

# Determine discount eligibility based on monthly usage
if monthly_usage <= 50:
    discount = 0
elif monthly_usage <= 100:
    discount = monthly_usage * 0.05
else:
    discount = monthly_usage * 0.20

# Calculate final bill after subtracting monthly usage and discount
final_bill = monthly_usage - discount

# Print the results with 2 decimals places
print()
print(f"Monthly usage: RM{monthly_usage:.2f}")
print(f"Discount: RM{discount:.2f}")
print(f"Final bill: RM{final_bill:.2f}")

# Prompt user input
Age = int(input("Enter your age: "))
TicketPrice = float(input("Enter ticket price of the movie ticket: "))

# Validate input (check for negative values)
if Age < 0 or TicketPrice < 0:
    print("ERROR: Age and Ticket Price cannot be negative value")
else:

    # Determine discount rate and category based on age
    if Age <= 12:
        DiscountRate = 0.5
        Category = "Children"
    elif Age >= 13 and Age <= 17:
        DiscountRate = 0.25
        Category = "Teenagers"
    else:
        DiscountRate = 0
        Category = "Adults"
   
    # Calculate final price after discount
    FinalPrice = TicketPrice - (TicketPrice * DiscountRate)

    # Display result
    print(f"\nYou are eligible for the {Category} discount ({DiscountRate * 100}%)")
    print(f"Discounted ticket price: ${FinalPrice:.2f}")
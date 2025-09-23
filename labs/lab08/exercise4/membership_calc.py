base_membership = 120

# Personal training sessions fee and number of sessions booked
personal_training_fee = 80
num_sessions = 6
training_total = personal_training_fee * num_sessions

# Additional Services
locker_rental = 25
towel_service = 15

# One-time registration fee 
registration_fee = 50

# Calculations
first_month_cost = base_membership + training_total + locker_rental + towel_service + registration_fee
monthly_cost = base_membership + training_total + locker_rental + towel_service
annual_cost = first_month_cost + (monthly_cost * 12)

# Display results
print("FITNESS MEMBERSHIP CALCULATOR")
print("-------------------------------")
print(f"Base Membership Fee: RM{base_membership}")
print(f"Personal Training Sessions: RM{training_total} ({num_sessions} sessions at RM{personal_training_fee} each) ")
print("------ Additional Services ------")
print(f"Locker Rental: RM{locker_rental}")
print(f"Towel Service: RM{towel_service}")
print("-------------------------------")
print(f"Total First-Month Cost: RM{first_month_cost}")
print(f"Monthly Cost: RM{monthly_cost}")
print(f"Annual Cost (12 months): RM{annual_cost}")
print(f"\nSEE YOU AGAIN!")

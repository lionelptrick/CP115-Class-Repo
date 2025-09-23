print("--- Restaurant Bill Calculator ---")

TotalDishesPrice = (3*25) + (2*12) + (4*8)
TotalBill = ((TotalDishesPrice * 110/100) + 5)
BillEachPerson = TotalBill // 6

print(f"\nTotal Dishes Price: RM{TotalDishesPrice}")
print(f"Total Bill: RM{TotalBill}")
print(f"Each person needs to pay: RM{BillEachPerson}")

print("\n--- Please come again! ---")
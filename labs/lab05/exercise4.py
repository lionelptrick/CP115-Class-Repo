print("--- Welcome to the Shopping Cost Calculator ---")
print("This program will calculate your shopping cart!")

print()
item_name = str(input("Enter your item name: "))
price = float(input("Enter the price of item: "))

quantity = 3
tax_rate = 0.06

subtotal = price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

print("\n --- RECEIPT ---")
print("Item: " + item_name)
print(f"Subtotal: RM {subtotal:.2f}")
print(f"Tax amount: RM {tax_amount:.2f}")
print(f"Total cost: RM {total_cost:.2f}")
print("-------------------")





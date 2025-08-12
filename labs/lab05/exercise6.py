print("\n --- Time Converter ---")

minutes = float(input("Enter time in minutes: "))

hours = minutes/60
remainder = minutes % 60

print(f"Original minutes: {minutes}")
print(f"Converted time: {hours:.2f} hours and remaining {minutes} ")
import math

print("\n --- Welcome to Circle Calculator --- ")

print("\nPlease enter the required value!")
radius = int(input("Radius: "))
circle_area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"\nThe area of a circle: {circle_area:.2f}")
print(f"The circumference of a circle: {circumference:.2f}")

print("\n --- Thank You for using Circle Calculator! ---")

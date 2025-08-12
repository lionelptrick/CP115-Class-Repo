import random

print("\n--- Thank you using Random Student Selector System! ---")
      
class_name = input("\nEnter your class name: ")

student_number = random.randint(1, 20)

print()
print(f"Randomly selected students from class {class_name}: Student #{student_number}")

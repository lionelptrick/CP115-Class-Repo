print("\n-- Welcome to the Student Information System! --")
print("This program will store your information..")


student_name = input("\nEnter your name: ")
student_age = int(input("Enter your age: "))
course_code = input("Enter your course code: ")

print("\n--- Student's Information ---")
print("Name: " + student_name)
print("Age: "+ str(student_age))
print("Course: "+ course_code)

print("\n --- Data Types ---")
print("Type of name:", type(student_name))
print("Type of age:", type(student_age))
print("Type of course code:", type(course_code))
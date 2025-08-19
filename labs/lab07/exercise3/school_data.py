import random

# Student's information
student_name = "LIONEL ANAK PATRICK PAT"
student_ID = 1317
age = 18

# Course's information
course_code = "CP115"
course_name = "Computer Programming"

# Random score between 70-95 and 75-100
score1 = random.randint(70, 95)
score2 = random.randint(75, 100)

# Total score
total_score = score1 + score2

# String operations on student name
name_upper = student_name.upper()
name_lower = student_name.lower()
name_length = len(student_name)

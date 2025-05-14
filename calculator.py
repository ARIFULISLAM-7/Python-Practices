
grade_points = {"A+": 4.0,
                "A": 4.0,
                "A-": 3.7,
                "B+": 3.3,
                "B": 3.0,
                "B-": 2.7,
                "C+": 2.3,
                "C": 2.0,
                "C-": 1.7,
                "D+": 1.3,
                "D": 1.0,
                "D-": 0.7,
                "F": 0 }
num_of_subject = int(input("Enter the number of subjects:"))
total_gpa = 0
count = 0
while count < num_of_subject:
    course = input("Enter the course name: ")
    grade = input("Enter the letter grade: ")
    grade = grade.upper()
    if grade not in grade_points:
        print("Invalid! Enter a valid grade.")
        continue
    print(f"{course.capitalize()}:{grade}")
    confirmation = input("Is this entry correct? [Yes/No]")
    if confirmation.lower() != "yes":
        continue
    total_gpa += grade_points[grade]
    count += 1
    average_gpa = total_gpa / count
    print(f"your gpa is {average_gpa}.")


"""
🏆 Grade Calculator
Input marks for five subjects and calculate the average and final grade.
"""
grades = []
for i in range(5):
    while True:
        try:
            grade = int(input("Enter a grade: "))
            grades.append(grade)
            break
        except ValueError:
            print("Please enter a numerical value")
average_grade = sum(grades) / len(grades)

if round(average_grade) >= 90:
    print("Your overall grade is A! Excellent job!🎉")
elif round(average_grade) >= 80:
    print("Your overall grade is B! Good job!👏🏽")
elif round(average_grade) >= 70:
    print("Your overall grade is C! You can do better!📚")
elif round(average_grade) >= 60:
    print("Your overall grade is D! Please study harder!📓")
else:
    print("Your overall grade is F! You have failed the course!😟")
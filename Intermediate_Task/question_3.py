# Student Result System

marks = [78, 85, 62, 90, 55]


def result_system(marks):
    total_marks = 0
    for n in marks:
        total_marks += n

    percentage = (total_marks / (len(marks) * 100)) * 100
    grade = ""

    if percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    return f"Total Marks: {total_marks} \nPercentage: {percentage} \nGrade: {grade}"


print(result_system(marks))

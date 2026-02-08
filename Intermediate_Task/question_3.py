# Student Result System

marks = [78, 85, 62, 90, 55]


def result_system(marks):
    if len(marks) == 0:
        return "No marks provided"

    total_marks = sum(marks)
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

    return f"Total Marks: {total_marks} \nPercentage: {percentage}% \nGrade: {grade}"


print(result_system(marks))

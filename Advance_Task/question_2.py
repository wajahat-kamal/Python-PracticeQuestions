# Attendance Tracker

attendance = ["present", "absent", "present", "present", "absent"]


def attendance_tracker(attendance):
    total = len(attendance)
    present = 0
    absent = 0

    for i in attendance:
        if i == "present":
            present += 1
        else:
            absent += 1

    percentage = (present / total) * 100

    return f"Total Students are: {total} \n Present {present} \n Absent {absent} \n Attendance Percentage: {percentage}%"


print(attendance_tracker(attendance))

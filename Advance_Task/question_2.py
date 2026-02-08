# Attendance Tracker

attendance = ["present", "absent", "present", "present", "absent"]


def attendance_tracker(attendance):
    present = 0
    absent = 0

    for i in attendance:
        if i == "present":
            present += 1
        else:
            absent += 1

    return (
        f"Total Students are: {len(attendance)} \n Present {present} \n Absent {absent}"
    )


print(attendance_tracker(attendance))

# Attendance Tracker

attendance = ["present", "absent", "present", "present", "absent"]


def attendance_tracker(attendance):
    present = []
    absent = []

    for i in attendance:
        if i == "present":
            present.append(i)
        else:
            absent.append(i)

    f"Present {len(present)} \n Absent {len(absent)}"

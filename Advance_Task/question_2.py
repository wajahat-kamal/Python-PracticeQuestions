# Attendance Tracker

attendance = ["present", "absent", "present", "present", "absent"]

present = []
absent = []

for i in attendance:
    if i == "present":
        present.append(i)
    else:
        absent.append(i)

print(present)
print(absent)
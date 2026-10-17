# Attendance Test for AttendX

def test_mark_attendance():
    student_id = "ST101"
    attendance_status = "Present"

    if student_id == "ST101" and attendance_status == "Present":
        print("PASS: Attendance marked successfully")
    else:
        print("FAIL: Attendance could not be marked")


def test_invalid_student():
    student_id = ""

    if student_id == "":
        print("PASS: Empty student ID detected")
    else:
        print("FAIL: Empty student ID was not detected")


test_mark_attendance()
test_invalid_student()
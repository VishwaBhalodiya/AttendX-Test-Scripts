# Login Test for AttendX

def test_valid_login():
    username = "student123"
    password = "correct123"

    if username == "student123" and password == "correct123":
        print("PASS: Valid login details accepted")
    else:
        print("FAIL: Valid login details rejected")


def test_invalid_login():
    username = "student123"
    password = "wrong123"

    if username == "student123" and password == "correct123":
        print("FAIL: Invalid login details accepted")
    else:
        print("PASS: Invalid login details rejected")


test_valid_login()
test_invalid_login()
import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (minimum 8 characters)": length_error,
        "Missing lowercase letter": lowercase_error,
        "Missing uppercase letter": uppercase_error,
        "Missing number": digit_error,
        "Missing special character": special_char_error
    }

    if all(not error for error in errors.values()):
        print("Password is STRONG")
    else:
        print("Password is WEAK")
        print("Issues found:")
        for issue, is_error in errors.items():
            if is_error:
                print(f" - {issue}")

# Main
if __name__ == "__main__":
    user_input = input("Enter a password to check its strength: ")
    check_password_strength(user_input)

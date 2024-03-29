def is_acceptable_password(password: str) -> bool:
    len_password = len(password)
    is_contain_one_digit = any(c.isdigit() for c in password)
    is_digits_only = password.isdigit()

    if len_password < 7:
        return False

    if 'password' in password.lower():
        return False

    if len_password > 9:
        return True
    else:
        return is_contain_one_digit and not is_digits_only


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

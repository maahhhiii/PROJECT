def validate_password_strength(password):
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if not (has_digit and has_upper and has_lower and has_special):
        raise ValueError("Password must include uppercase, lowercase, digit, and special character.")
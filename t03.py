def check_password_strength(password):
    strength = 0

    if len(password) >= 8:  # Minimum length of 8
        strength += 1
    if any(char.isupper() for char in password):  # At least one uppercase letter
        strength += 1
    if any(char.islower() for char in password):  # At least one lowercase letter
        strength += 1
    if any(char.isdigit() for char in password):  # At least one number
        strength += 1
    if any(char in "!@#$%^&*()-_=+{}[]|:;'<>,.?/" for char in password):  # Special character
        strength += 1

    if strength == 5:
        return "Strong Password"
    elif 3 <= strength < 5:
        return "Moderate Password"
    else:
        return "Weak Password"

password = input("Enter a password to check its strength: ")
result = check_password_strength(password)
print(f"Password Strength: {result}")



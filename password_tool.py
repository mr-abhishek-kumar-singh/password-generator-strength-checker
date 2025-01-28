import random
import string

def generate_password(length=12):
    """
    Generates a random password containing uppercase, lowercase, digits, and special characters.

    Args:
        length (int): Length of the password (default is 12).

    Returns:
        str: The generated password.
    """
    if length < 4:
        return "Error: Password length must be at least 4 for sufficient complexity."
    
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_strength(password):
    """
    Checks the strength of the given password.

    Args:
        password (str): The password to check.

    Returns:
        str: Strength evaluation of the password.
    """
    if len(password) < 8:
        return "Weak: Too short"
    if not any(c.islower() for c in password):
        return "Weak: No lowercase letter"
    if not any(c.isupper() for c in password):
        return "Weak: No uppercase letter"
    if not any(c.isdigit() for c in password):
        return "Weak: No number"
    if not any(c in string.punctuation for c in password):
        return "Weak: No special character"
    return "Strong"

# Get user input for password generation length
try:
    length = int(input("Enter the desired password length (default: 12): ") or 12)
    password = generate_password(length)
    if "Error" in password:
        print(password)
    else:
        print(f"Generated password: {password}")
        print(f"Strength: {check_strength(password)}")
except ValueError:
    print("Error: Please enter a valid integer for the password length.")

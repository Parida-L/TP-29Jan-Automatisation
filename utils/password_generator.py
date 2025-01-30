import random
import string

def generate_secure_password(length=12):
    """
    Generates a secure password that meets the following criteria:
    - At least one uppercase letter (A-Z)
    - At least one lowercase letter (a-z)
    - At least one digit (0-9)
    - At least one special character (!@#$%^&*()-_=+)
    - Minimum length of 8 characters
    """

    if length < 8:
        raise ValueError("Password must be at least 8 characters long.")

    # Required character types
    uppercase = random.choice(string.ascii_uppercase)  # A-Z
    lowercase = random.choice(string.ascii_lowercase)  # a-z
    digit = random.choice(string.digits)  # 0-9
    special_char = random.choice("!@#$%^&*()-_=+")  # Special characters

    # Fill the remaining characters randomly
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    remaining_chars = [random.choice(all_characters) for _ in range(length - 4)]

    # Combine all required characters
    password_list = [uppercase, lowercase, digit, special_char] + remaining_chars
    random.shuffle(password_list)  # Shuffle to avoid predictable order

    # Convert list to string
    secure_password = ''.join(password_list)

    return secure_password

# Example usage
print("Generated Secure Password:", generate_secure_password())

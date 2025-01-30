import random

def generate_unique_username(base_username="Scarface"):
    """Generates a unique username by appending random numbers and special characters."""
    special_chars = "!@#$%^&*"
    digits = "0123456789"

    random_number = ''.join(random.choices(digits, k=3))
    random_special = ''.join(random.choices(special_chars, k=2))

    return f"{base_username}{random_number}{random_special}"

import random
import string

def generate_password(length=12):
    if length < 4:  # Ensure sufficient length for a strong password
        raise ValueError("Password length must be at least 4 characters.")

    # Define character pools
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure password has at least one character from each pool
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(password_length))
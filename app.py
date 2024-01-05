import random
import string

def generate_password(length=12):
    # Characters to generate password with
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Setdesired password length
password_length = 12

# Generate and print a password
generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")

import random
import string

def generate_password(length=12):
    """
    Generate a random password.

    Parameters:
    length (int): The desired length of the password. Defaults to 12.

    Returns:
    str: A randomly generated password containing uppercase letters,
         lowercase letters, digits, and special characters.
    """
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # string.ascii_letters includes both lowercase and uppercase letters
    # string.digits includes numbers 0-9
    # string.punctuation includes special characters like !, @, #, etc.

    # Generate password by randomly selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Ask user for password length
password_length = input("Enter the length of the password (default is 12): ")

# Validate user input and set default if input is invalid
if password_length.isdigit():
    password_length = int(password_length)
else:
    password_length = 12  # Default length

# Generate and print password
password = generate_password(password_length)
print("Generated Password:", password)

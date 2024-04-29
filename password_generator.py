import random
import string

def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Ask user for password length
password_length = input("Enter the length of the password (default is 12): ")
if password_length.isdigit():
    password_length = int(password_length)
else:
    password_length = 12

# Generate and print password
password = generate_password(password_length)
print("Generated Password:", password)
#Developer: Elliot Fahl
#Date: 3/14/2024


import hashlib
import getpass

def hash_password(password, salt):
    # Combine password and salt
    salted_password = password.encode() + salt.encode()
    # Hash the combined password and salt using SHA-256
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password

if __name__ == "__main__":
    # Get password from user input without showing characters
    password = getpass.getpass(prompt="Enter your password: ")
    # Generate a random salt (you may use a different method to generate salts)
    salt = "somerandomsalt"
    # Hash the password with the salt
    hashed_password = hash_password(password, salt)
    # Print the hashed password
    print("Hashed password:", hashed_password)
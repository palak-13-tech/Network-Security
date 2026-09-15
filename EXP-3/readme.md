import hashlib
import random

# Stored user details
username = "admin"
password = "1234"

# Generate a challenge
challenge = str(random.randint(1000, 9999))

print("Challenge:", challenge)

# User enters 
user = input("Enter username: ")
pwd = input("Enter password: ")

# Generate response using password + challenge
response = hashlib.sha256((pwd + challenge).encode()).hexdigest()

# Check authentication
if user == username and pwd == password:
    print("Authentication Successful!")
    print("Response:", response)

# Simulate replay attack
    print("\nTrying to reuse the same response...")
    print("Replay Attack Detected!")
else:
    print("Authentication Failed!")

import random
import hashlib

SECRET = "1234"

# Generate a random challenge
def generate_challenge():
    return str(random.randint(1000, 9999))

# Generate response
def generate_response(challenge):
    return hashlib.sha256(
        (challenge + SECRET).encode()
    ).hexdigest()

print("=== CHALLENGE-RESPONSE AUTHENTICATION ===")

# Server generates challenge
challenge = generate_challenge()
print("Server Challenge:", challenge)

# Client generates response
response = generate_response(challenge)
print("Client Response:", response)

# Server verifies response
expected_response = generate_response(challenge)

if response == expected_response:
    print("Authentication: SUCCESS")
else:
    print("Authentication: FAILED")


print("\n=== REPLAY ATTACK SIMULATION ===")

# Attacker captures old response
captured_response = response
print("Captured Old Response:", captured_response)

# Server generates a new challenge
new_challenge = generate_challenge()
print("New Server Challenge:", new_challenge)

# Attacker tries old response
expected_new_response = generate_response(new_challenge)

if captured_response == expected_new_response:
    print("Replay Attack: SUCCESS")
else:
    print("Replay Attack: BLOCKED")

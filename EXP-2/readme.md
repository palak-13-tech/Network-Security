import hashlib
text = input("Enter text: ")

original_hash = hashlib.sha256(text.encode()).hexdigest()

print("\nOriginal Hash:", original_hash)

# Modify 
modified_text = input("\nEnter modified text: ")

# Generate modified hash
modified_hash = hashlib.sha256(modified_text.encode()).hexdigest()

print("Modified Hash:", modified_hash)

# Compare 
if original_hash == modified_hash:
    print("\nData is unchanged. Integrity verified.")
else:
    print("\nData has been modified/tampered!")

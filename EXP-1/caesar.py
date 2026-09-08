def encrypt(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)

    return result


text = input("Enter the text: ").upper()
shift = int(input("Enter the shift: "))

cipher = encrypt(text, shift)
print("Encrypted:", cipher)

print("Decrypted:", encrypt(cipher, -shift))

text = input("Enter the text: ").upper()
key = input("Enter the key: ").upper()
def encrypt(text, key):
    result = ""
    j = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[j]) - ord("A")
            new = (ord(char) - ord("A") + shift) % 26
            result += chr(ord("A") + new)
            j = (j + 1) % len(key)
        else:
            result += char

    return result
def decrypt(text, key):
    result = ""
    j = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[j]) - ord("A")
            new = (ord(char) - ord("A") - shift) % 26
            result += chr(ord("A") + new)
            j = (j + 1) % len(key)
        else:
            result += char
    return result
encrypted = encrypt(text, key)
print("Encrypted:", encrypted)

print("Decrypted:", decrypt(encrypted, key))

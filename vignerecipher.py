import string

def vigenere_encrypt(plaintext, key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    ciphertext = ""
    key_index = 0
    for char in plaintext.lower():
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            new_char = alphabet[(alphabet.index(char) + shift) % 26]
            ciphertext += new_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    plaintext = ""
    key_index = 0
    for char in ciphertext.lower():
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            new_char = alphabet[(alphabet.index(char) - shift) % 26]
            plaintext += new_char
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext

# Example usage
plaintext = "she is listening"
key = "PASCAL"
ciphertext = vigenere_encrypt(plaintext, key)
decrypted_text = vigenere_decrypt(ciphertext, key)
print("Ciphertext:", ciphertext.upper())
print("Decrypted Text:", decrypted_text)
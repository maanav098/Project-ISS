from Cryptodome.Cipher import DES
import binascii
import os

def pad(text):
    """Add PKCS#7 padding to make text a multiple of 8 bytes"""
    padding_length = 8 - (len(text) % 8)
    return text + bytes([padding_length]) * padding_length

def unpad(text):
    """Remove PKCS#7 padding"""
    return text[:-text[-1]]

def encrypt_des(plaintext, key=None):
    """Encrypt plaintext using DES"""
    if key is None:
        key = os.urandom(8)  # Generate random 8-byte key
    
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext))
    
    return {
        'ciphertext': binascii.hexlify(ciphertext).decode('utf-8'),
        'key': binascii.hexlify(key).decode('utf-8')
    }

def decrypt_des(ciphertext_hex, key_hex):
    """Decrypt ciphertext using DES"""
    key = binascii.unhexlify(key_hex)
    ciphertext = binascii.unhexlify(ciphertext_hex)
    
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    
    return unpad(padded_plaintext).decode('utf-8')

# Example usage
if __name__ == "__main__":
    message = "Hello, DES!"
    print(f"Original: {message}")
    
    # Encrypt
    result = encrypt_des(message)
    print(f"Key: {result['key']}")
    print(f"Encrypted: {result['ciphertext']}")
    
    # Decrypt
    decrypted = decrypt_des(result['ciphertext'], result['key'])
    print(f"Decrypted: {decrypted}")
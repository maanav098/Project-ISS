import numpy as np

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    a = a % m
    if a == 0:
        raise ValueError(f"No inverse exists for {a} under modulo {m}")
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def matrix_mod_inv_2x2(matrix, modulus):
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    det = (a * d - b * c) % modulus
    det_inv = mod_inverse(det, modulus)
    return np.array([
        [( d * det_inv) % modulus, ((-b) * det_inv) % modulus],
        [((-c) * det_inv) % modulus, ( a * det_inv) % modulus]
    ])

def process_text(text, block_size):
    text = ''.join(filter(str.isalpha, text.upper()))
    padding = block_size - (len(text) % block_size)
    if padding != block_size:
        text += 'X' * padding
    return text

def text_to_numeric(text):
    return [ord(char) - ord('A') for char in text]

def numeric_to_text(nums):
    return ''.join(chr(num + ord('A')) for num in nums)

def hill_encrypt(plaintext, key_matrix):
    block_size = key_matrix.shape[0]
    plaintext = process_text(plaintext, block_size)
    plaintext_nums = text_to_numeric(plaintext)
    ciphertext_nums = []
    for i in range(0, len(plaintext_nums), block_size):
        block = np.array(plaintext_nums[i:i+block_size])
        encrypted_block = key_matrix.dot(block) % 26
        ciphertext_nums.extend(encrypted_block)
    return numeric_to_text(ciphertext_nums)

def hill_decrypt(ciphertext, key_matrix):
    block_size = key_matrix.shape[0]
    ciphertext = process_text(ciphertext, block_size)
    ciphertext_nums = text_to_numeric(ciphertext)
    inv_key_matrix = matrix_mod_inv_2x2(key_matrix, 26)
    decrypted_nums = []
    for i in range(0, len(ciphertext_nums), block_size):
        block = np.array(ciphertext_nums[i:i+block_size])
        decrypted_block = inv_key_matrix.dot(block) % 26
        decrypted_nums.extend(decrypted_block.astype(int))
    decrypted_text = numeric_to_text(decrypted_nums)
    decrypted_text = decrypted_text.rstrip('X')
    return decrypted_text

def main():
    import math
    key = [
        [3, 3],
        [2, 5]
    ]
    key_matrix = np.array(key)
    a, b = key_matrix[0]
    c, d = key_matrix[1]
    det = (a * d - b * c) % 26
    if gcd(det, 26) != 1:
        raise ValueError("The key matrix is not invertible modulo 26.")
    plaintext = "HELLO"

    ciphertext = hill_encrypt(plaintext, key_matrix)
    decrypted = hill_decrypt(ciphertext, key_matrix)

    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted:  {decrypted}")

if __name__ == "__main__":
    main()

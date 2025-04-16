import random

# Function to perform modular exponentiation
def power(base, exponent, modulus):
    return pow(base, exponent, modulus)

# Diffie-Hellman parameters (can be agreed upon publicly)
# Prime number (p) and primitive root modulo p (g)
p = 23  # a small prime number for simplicity
g = 5   # a primitive root modulo 23

# Private keys (chosen secretly by Alice and Bob)
a_private = random.randint(1, p-2)  # Alice's private key
b_private = random.randint(1, p-2)  # Bob's private key

# Public keys (shared with each other)
A_public = power(g, a_private, p)  # Alice's public key
B_public = power(g, b_private, p)  # Bob's public key

# Shared secret key (computed independently by both)
shared_secret_alice = power(B_public, a_private, p)
shared_secret_bob = power(A_public, b_private, p)

# Output results
print(f"Prime (p): {p}")
print(f"Base (g): {g}")
print(f"Alice's Private Key: {a_private}")
print(f"Bob's Private Key: {b_private}")
print(f"Alice's Public Key: {A_public}")
print(f"Bob's Public Key: {B_public}")
print(f"Alice's Shared Secret: {shared_secret_alice}")
print(f"Bob's Shared Secret: {shared_secret_bob}")
print(f"Shared Secret Match: {shared_secret_alice == shared_secret_bob}")

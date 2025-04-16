import hashlib

def generate_hashes(input_string):
    # Encode the input string
    encoded = input_string.encode()

    # Create MD5 hash
    md5_hash = hashlib.md5(encoded).hexdigest()

    # Create SHA-256 hash
    sha256_hash = hashlib.sha256(encoded).hexdigest()

    return md5_hash, sha256_hash

# Example usage
if __name__ == "__main__":
    message = input("Enter the message to hash: ")
    md5_result, sha256_result = generate_hashes(message)

    print(f"\nOriginal Message: {message}")
    print(f"MD5 Hash: {md5_result}")
    print(f"SHA-256 Hash: {sha256_result}")

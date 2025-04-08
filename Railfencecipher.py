# Rail Fence Cipher Implementation

def encrypt_rail_fence(text, key):
    """
    Encrypts text using Rail Fence cipher with specified number of rails (key)
    """
    # Remove spaces from the text
    text = text.replace(" ", "")
    
    # Create the matrix (rails)
    rails = [[] for _ in range(key)]
    
    # Direction flag: True means moving down, False means moving up
    direction_down = False
    
    # Current rail
    rail = 0
    
    # Populate the rails
    for char in text:
        # Add character to current rail
        rails[rail].append(char)
        
        # Change direction if we reached the top or bottom rail
        if rail == 0 or rail == key - 1:
            direction_down = not direction_down
        
        # Move to next rail (up or down)
        if direction_down:
            rail += 1
        else:
            rail -= 1
    
    # Construct the ciphertext from the rails
    ciphertext = ""
    for rail in rails:
        ciphertext += "".join(rail)
    
    return ciphertext

def decrypt_rail_fence(ciphertext, key):
    """
    Decrypts ciphertext that was encrypted using Rail Fence cipher with specified key
    """
    # Create the matrix (rails)
    rails = [[] for _ in range(key)]
    
    # Calculate the positions in the rails first
    rail_positions = []
    rail = 0
    direction_down = False
    
    for i in range(len(ciphertext)):
        rail_positions.append(rail)
        
        # Change direction if we reached the top or bottom rail
        if rail == 0 or rail == key - 1:
            direction_down = not direction_down
        
        # Move to next rail (up or down)
        if direction_down:
            rail += 1
        else:
            rail -= 1
    
    # Calculate how many characters go in each rail
    rail_sizes = [rail_positions.count(i) for i in range(key)]
    
    # Fill the rails with placeholder characters
    index = 0
    for i in range(key):
        rails[i] = list(ciphertext[index:index + rail_sizes[i]])
        index += rail_sizes[i]
    
    # Reconstruct the plaintext by reading in zigzag pattern
    plaintext = ""
    rail = 0
    direction_down = False
    
    for _ in range(len(ciphertext)):
        plaintext += rails[rail].pop(0)
        
        # Change direction if we reached the top or bottom rail
        if rail == 0 or rail == key - 1:
            direction_down = not direction_down
        
        # Move to next rail (up or down)
        if direction_down:
            rail += 1
        else:
            rail -= 1
    
    return plaintext

# Row-Column Transformation Cipher Implementation

def encrypt_row_column(text, key):
    """
    Encrypts text using Row-Column Transformation with a keyword
    """
    # Remove spaces and convert to uppercase
    text = text.replace(" ", "").upper()
    key = key.upper()
    
    # Calculate number of columns (length of key)
    cols = len(key)
    
    # Calculate number of rows needed
    rows = -(-len(text) // cols)  # Ceiling division
    
    # Pad the text if necessary
    if len(text) % cols != 0:
        text += 'X' * (cols - len(text) % cols)
    
    # Create the matrix
    matrix = []
    for i in range(0, len(text), cols):
        matrix.append(list(text[i:i+cols]))
    
    # Determine the column order based on the key
    key_order = [(char, i) for i, char in enumerate(key)]
    key_order.sort()  # Sort by the key characters
    column_order = [i for _, i in key_order]
    
    # Read the columns in the order determined by the key
    ciphertext = ""
    for col in column_order:
        for row in range(rows):
            ciphertext += matrix[row][col]
    
    return ciphertext

def decrypt_row_column(ciphertext, key):
    """
    Decrypts ciphertext that was encrypted using Row-Column Transformation with a keyword
    """
    # Convert key to uppercase
    key = key.upper()
    
    # Calculate number of columns (length of key)
    cols = len(key)
    
    # Calculate number of rows
    rows = len(ciphertext) // cols
    
    # Determine the column order based on the key
    key_order = [(char, i) for i, char in enumerate(key)]
    key_order.sort()  # Sort by the key characters
    column_order = [i for _, i in key_order]
    
    # Create an empty matrix
    matrix = [[''] * cols for _ in range(rows)]
    
    # Fill the matrix column by column in the order determined by the key
    index = 0
    for col in column_order:
        for row in range(rows):
            matrix[row][col] = ciphertext[index]
            index += 1
    
    # Read the matrix row by row
    plaintext = ""
    for row in range(rows):
        plaintext += ''.join(matrix[row])
    
    return plaintext

# Example usage
if __name__ == "__main__":
    # Test Rail Fence Cipher
    plaintext = "DEFENDTHEEASTWALLOFTHECASTLE"
    key_rail = 3
    
    rail_encrypted = encrypt_rail_fence(plaintext, key_rail)
    print(f"Rail Fence Encryption (key={key_rail}):")
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {rail_encrypted}")
    
    rail_decrypted = decrypt_rail_fence(rail_encrypted, key_rail)
    print(f"Decrypted: {rail_decrypted}")
    print()
    
    # Test Row-Column Transformation Cipher
    plaintext = "ENEMYATTACKSTONIGHT"
    key_rc = "CRYPTO"
    
    rc_encrypted = encrypt_row_column(plaintext, key_rc)
    print(f"Row-Column Transformation (key={key_rc}):")
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {rc_encrypted}")
    
    rc_decrypted = decrypt_row_column(rc_encrypted, key_rc)
    print(f"Decrypted: {rc_decrypted}")
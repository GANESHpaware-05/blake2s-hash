import hashlib

def generate_blake2s(input_text):
    
    # Convert input text to bytes
    input_bytes = input_text.encode('utf-8')

    # Generate BLAKE2s hash
    hash_blake2s = hashlib.blake2s(input_bytes).hexdigest()

    return hash_blake2s

# Example usage:
input_text = input("Enter the text to hash: ")
hash_result = generate_blake2s(input_text)
print("BLAKE2s hash:", hash_result)
import hashlib

def create_sha256_hash(text):
    """
    Ye function text ko leta hai aur usey secure SHA-256 
    hash mein convert kar deta hai.
    """
    # 1. Text ko bytes mein encode karein
    encoded_text = text.encode('utf-8')
    
    # 2. Hashlib use karke hash banayein
    hash_object = hashlib.sha256(encoded_text)
    
    # 3. Hash ko hexadecimal format mein convert karein
    hex_hash = hash_object.hexdigest()
    
    return hex_hash

# --- Main Program ---
if __name__ == "__main__":
    print("--- Simple Hashing Tool V1.0 ---")
    
    # Example Input (Tum isay change kar sakte ho)
    my_input = "CyberSecurity is the Future"
    
    # Hash Generate karein
    hashed_result = create_sha256_hash(my_input)
    
    # Result Print karein
    print(f"Original Text: {my_input}")
    print(f"SHA-256 Hash:  {hashed_result}")
  

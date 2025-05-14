import os
import hashlib
import base64

def hash_password(password, iterations=100_000):
    """
    Hashes the password using PBKDF2 with SHA-256.
    
    Returns:
        salt (hex string), hashed_password (base64 string)
    """
    salt = os.urandom(16)  # Generate 16-byte random salt
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations)
    return salt.hex(), base64.b64encode(dk).decode()

import string
import random

def get_qrandom_bits(n_bits):
    """
    Simulates quantum random bits using Python's random module
    (fallback for cloud platforms where Qiskit Aer is not supported)
    """
    return ''.join(str(random.getrandbits(1)) for _ in range(n_bits))

def generate_password(length=16):
    charset = string.ascii_letters + string.digits + string.punctuation
    bits = get_qrandom_bits(length * 8)
    password = ''
    for i in range(length):
        segment = bits[i*8:(i+1)*8]
        index = int(segment, 2) % len(charset)
        password += charset[index]
    return password


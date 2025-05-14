from qiskit import QuantumCircuit, Aer, execute
import string

def get_qrandom_bits(n_bits):
    """Generates n_bits of quantum randomness using Hadamard gates."""
    qc = QuantumCircuit(n_bits, n_bits)
    qc.h(range(n_bits))  # Put all qubits in superposition
    qc.measure(range(n_bits), range(n_bits))  # Measure them
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1).result()
    bits = list(result.get_counts().keys())[0][::-1]  # Reverse due to qiskit's bit ordering
    return bits

def generate_password(length=16):
    """Converts quantum random bits into a strong password of specified length."""
    charset = string.ascii_letters + string.digits + string.punctuation
    bits = get_qrandom_bits(length * 8)  # 8 bits per character
    password = ''
    for i in range(length):
        segment = bits[i*8:(i+1)*8]
        index = int(segment, 2) % len(charset)
        password += charset[index]
    return password

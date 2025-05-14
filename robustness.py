from math import log2
import string

def shannon_entropy(password):
    """
    Calculates the Shannon entropy of the password.
    """
    prob = [password.count(c) / len(password) for c in set(password)]
    return round(-sum(p * log2(p) for p in prob), 2)

def guess_estimate(password):
    """
    Estimates the entropy in bits and guess count based on character set used.
    """
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)

    entropy_bits = len(password) * log2(charset)
    guesses = 2 ** entropy_bits
    return round(entropy_bits, 2), f"{guesses:.2e}"

def audit_password(password):
    """
    Combines entropy and guess estimation for a given password.
    Returns a dictionary with both metrics.
    """
    entropy, guess_count = guess_estimate(password)
    return {
        "entropy": shannon_entropy(password),
        "guess_count": guess_count
    }

import streamlit as st
from generator import generate_password
from robustness import audit_password
from hash_util import hash_password

st.title("🔐 Quantum Password Generator")

length = st.slider("Select password length", min_value=8, max_value=32, value=16)

if st.button("Generate Password"):
    password = generate_password(length)
    salt, hashed = hash_password(password)
    audit = audit_password(password)

    st.subheader("🧪 Password")
    st.code(password)

    st.subheader("🔐 PBKDF2 Hash")
    st.text_area("Hashed Output", hashed, height=100)

    st.subheader("📊 Strength Metrics")
    st.write(f"Shannon Entropy: `{audit['entropy']} bits`")
    st.write(f"Estimated Brute Force Guesses: `{audit['guess_count']}`")

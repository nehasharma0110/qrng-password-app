# 🔐 Quantum Random Password Generator

This project presents a secure password generation application that leverages **Quantum Random Number Generation (QRNG)** for entropy, uses **PBKDF2-HMAC-SHA256** for password hashing, and performs a multi-pronged **robustness evaluation** including entropy estimation, brute-force simulation, dictionary attack checks, and histogram analysis.

---

## 📌 Features

- Quantum entropy generation using Qiskit (or fallback for cloud)
- Converts quantum bits to strong, policy-compliant passwords
- Secure password hashing with PBKDF2 (salt + key stretching)
- Robustness analysis:
  - Shannon entropy calculation
  - Brute-force attack estimate
  - Dictionary attack simulation
  - Entropy histogram visualization
- Interactive UI built with Streamlit
- Modular codebase for reproducibility and publication

---

## 🧩 Architecture Overview

**Pipeline:**
Quantum Entropy → Password Generation → PBKDF2 Hashing → Robustness Evaluation
├─ Entropy Estimation
├─ Brute-force Attack
├─ Dictionary Attack
└─ Histogram Analysis  


---

## 🚀 How to Run

### Prerequisites

- Python 3.8+
- Install required libraries:
  ```bash
  pip install -r requirements.txt


Launch the Streamlit App
streamlit run app.py


📁 File Structure
├── app.py               # Main Streamlit UI
├── generator.py         # QRNG / random password generation
├── hash_util.py         # PBKDF2 hashing module
├── robustness.py        # Entropy + attack simulations
├── requirements.txt     # Dependencies
└── README.md            # Project overview

📊 Sample Evaluation Output
{
  "password": "zK9#Qh7&*Lp@",
  "shannon_entropy": 3.92,
  "brute_force_entropy": 104.7,
  "guess_estimate": "3.7e+31",
  "dictionary_hit": false,
  "hash": "pbkdf2:sha256$..."
}

📌 Notes
The entropy simulation works with Qiskit locally.

On Streamlit Cloud, QRNG may fall back to random.getrandbits() due to backend limitations.

📄 License
MIT License – free to use, modify, and distribute.

Authors: This repository supports academic research. Please cite appropriately if used in publications.

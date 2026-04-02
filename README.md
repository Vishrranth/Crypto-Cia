Gronsfeld Cipher with Custom Hashing


This project implements a two-stage cryptographic system:

Gronsfeld Cipher for encryption and decryption using a numeric key
Custom Hash Function to convert ciphertext into a numeric digest

The system demonstrates both reversible encryption and one-way hashing.


Theory:


Gronsfeld Cipher

The Gronsfeld cipher is a polyalphabetic substitution cipher similar to the Vigenère cipher, but it uses a numeric key (0–9).

Each letter is shifted using a digit from the key
The key repeats if it is shorter than the plaintext


Encryption Formula:
C = (P + K) mod 26

Decryption formula:
P = (C - K) mod 26

P = Plaintext letter position (0–25)
C = Ciphertext letter position
K = Key digit


H = (ASCII(c) + 3*i + 7) mod 26
D = H mod 10
c = character
i = position index
Output is a digit (0–9)

This function:

Uses ASCII values
Includes position-based variation
Produces a numeric output
Is one-way (not reversible)


Reason for Choosing this Hash Function
1. Simplicity and Ease of Implementation

The function uses:

Basic arithmetic operations
No external libraries

This makes it easy to implement in Python/C, suitable for academic projects.

2. Position-Based Variation

The inclusion of 3*i ensures that:

Same characters at different positions produce different outputs

This reduces repetition patterns in the hash output.

3. Deterministic Behavior

Same input → same output every time

Important for:

Testing
Verification
Consistency


4. Lightweight Computation
Uses only addition and modulo operations

Efficient and fast, even for longer inputs.




How to Run the Code
  Step 1: Run Encryption/Decryption
python Encrypt_Decrypt.py
  Step 2: Run Hash Function
python hash_function.py


Worked Examples
Example 1

Plaintext:snuchennai

Key:9876543210

Encryption: snuchennai → bvbimiqpbi

Hash Output: bvbimiqpbi → 1477438059


Decryption: bvbimiqpbi → snuchennai


Example 2

Plaintext:vishrranth

Key:9500433055

Encryption: vishrranth → enshvudnym

Hash Output: enshvudnym → 6284416259

Decryption: enshvudnym → vishrranth

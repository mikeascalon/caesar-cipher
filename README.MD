# LAB - Class 18

## Project: Cryptography

Author: Michelangelo Ascalon

## Overview

This project implements a simple Caesar Cipher, a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. The project includes functions to encrypt and decrypt text using this cipher, as well as a function to crack an encrypted message without the shift key.


## Setup
#### Dependencies
- Make sure Python is installed on your machine.
- Install necessary Python packages from `requirements.txt` using the command:
  ```bash
  pip install -r requirements.txt
  ```

## How to Run the Application

#### Encrypting and Decrypting Text

To use the cipher, run the `cipher.py` script.

Functions available:

* `encrypt(plain_text, shift)`: Encrypts the plain text using the provided shift.
* `decrypt(encrypted_text, shift)`: Decrypts the text using the provided shift.
* `crack(encrypted_text)`: Attempts to crack the encryption without the shift key.

```python
from caesar_cipher.cipher import encrypt, decrypt, crack

# Encrypt a message
encrypted_message = encrypt("Hello World", 5)
print("Encrypted:", encrypted_message)

# Decrypt a message
decrypted_message = decrypt(encrypted_message, 5)
print("Decrypted:", decrypted_message)

# Crack an encrypted message
cracked_message = crack(encrypted_message)
print("Cracked:", cracked_message)

```

#### Testing

To run tests, use the `test_caesar.py` script. Tests cover the following functionalities:

* Encrypting a string with a given shift.
* Decrypting a previously encrypted string with the same shift.
* Handling both uppercase and lowercase letters in encryption.
* Ignoring non-alphabetic characters, including whitespace, in encryption.
* Decrypting an encrypted version of a known phrase without knowing the shift used.


from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import os
from tqdm import tqdm  # Progress bar

# Generate AES key from password
def get_key_from_password(password):
    salt = b'secure_salt_value'  # Keep this constant
    return PBKDF2(password, salt, dkLen=32)

# Encrypt a file with a progress bar
def encrypt_file(input_file, output_file, password, progress_callback=None):
    key = get_key_from_password(password)
    cipher = AES.new(key, AES.MODE_CBC)

    with open(input_file, 'rb') as file:
        plaintext = file.read()

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_file, 'wb') as file:
        file.write(cipher.iv + ciphertext)

    if progress_callback:
        progress_callback(100)  # Update progress to 100%

    print(f"File '{input_file}' encrypted successfully as '{output_file}'")

# Decrypt a file with a progress bar
def decrypt_file(input_file, output_file, password, progress_callback=None):
    key = get_key_from_password(password)

    with open(input_file, 'rb') as file:
        file_data = file.read()

    iv = file_data[:AES.block_size]
    ciphertext = file_data[AES.block_size:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_file, 'wb') as file:
        file.write(plaintext)

    if progress_callback:
        progress_callback(100)  # Update progress to 100%

    print(f"File '{input_file}' decrypted successfully as '{output_file}'")

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key_size = 8

key = get_random_bytes(key_size)

iv = get_random_bytes(DES.block_size)
cipher = DES.new(key, DES.MODE_CFB, iv)

def encrypt_message(cipher, message):
    encrypted_message = cipher.encrypt(message.encode('utf-8'))
    return cipher.iv + encrypted_message

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:DES.block_size]
    encrypted_message = encrypted_message[DES.block_size:]
    cipher = DES.new(key, DES.MODE_CFB, iv)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode('utf-8')

message = "This is a test message."

encrypted_message = encrypt_message(cipher, message)

decrypted_message = decrypt_message(key, encrypted_message)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message.hex()}")
print(f"Decrypted Message: {decrypted_message}")

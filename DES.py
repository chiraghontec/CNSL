from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
import binascii

def encrypt_des(key,data):
    key = key.encode('utf-8')
    cipher = DES.new(key, DES.MODE_CBC)
    padded_data = pad(data.encode('utf-8'), DES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return binascii.hexlify(cipher.iv).decode('utf-8'), binascii.hexlify(encrypted_data).decode('utf-8')

def decrypt_des(key, iv, encrypted_data):
    key = key.encode('utf-8')
    iv = binascii.unhexlify(iv)
    encrypted_data = binascii.unhexlify(encrypted_data)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_data = unpad(decrypted_data, DES.block_size)
    return decrypted_data.decode('utf-8')
if __name__ == "__main__":
    key = '17012005'
    data = 'chirag'
    iv,encrypted_data = encrypt_des(key,data)
    print("encrypted data:", encrypted_data)
    print("IV:", iv)
    decrypted_data = decrypt_des(key, iv, encrypted_data)
    print("Decrypted data:", decrypted_data)
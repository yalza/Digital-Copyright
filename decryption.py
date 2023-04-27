from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Đọc nội dung của tệp tin đã được mã hóa
with open('ciphertext.bin', 'rb') as f:
    ciphertext = f.read()

# Đọc khóa bí mật từ file
with open('private_key.rar', 'rb') as f:
    private_key = RSA.import_key(f.read())

# Giải mã dữ liệu bằng khóa bí mật
cipher_rsa = PKCS1_OAEP.new(private_key)
plaintext = cipher_rsa.decrypt(ciphertext)

# Lưu dữ liệu đã được giải mã vào file
with open('decrypted_plaintext.enc', 'wb') as f:
    f.write(plaintext)
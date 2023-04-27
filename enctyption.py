from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Tạo cặp khóa RSA
key = RSA.generate(2048*5)

# Lưu khóa công khai vào file
with open('public_key.pem', 'wb') as f:
    f.write(key.publickey().export_key())

# Lưu khóa bí mật vào file
with open('private_key.pem', 'wb') as f:
    f.write(key.export_key())
    
    
# Đọc nội dung của tệp tin cần mã hóa
with open('Game.rar', 'rb') as f:
    plaintext = f.read()

# Đọc khóa công khai từ file
with open('public_key.pem', 'rb') as f:
    public_key = RSA.import_key(f.read())

# Mã hóa dữ liệu bằng khóa công khai
cipher_rsa = PKCS1_OAEP.new(public_key)
ciphertext = cipher_rsa.encrypt(plaintext)

# Lưu dữ liệu đã được mã hóa vào file
with open('ciphertext.bin', 'wb') as f:
    f.write(ciphertext)
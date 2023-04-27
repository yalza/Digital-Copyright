from Crypto.Cipher import AES
import os

# Tạo khóa và vector khởi tạo ngẫu nhiên
key = os.urandom(32)
iv = os.urandom(16)


file_object = open("text.txt", "w") # mở file ở chế độ ghi
file_object.write(key.hex()) # ghi dữ liệu vào file
file_object.close() # đóng file

# Tạo đối tượng AES cipher với khóa và IV đã tạo
cipher_aes = AES.new(key, AES.MODE_CFB, iv)

# Đọc dữ liệu từ file rar và mã hóa nó
with open('Game.rar', 'rb') as f_in:
    with open('Game.enc', 'wb') as f_out:
        # Ghi IV đầu tiên vào file đầu ra
        f_out.write(iv)

        # Đọc từng khối dữ liệu 16 byte, mã hóa và ghi vào file đầu ra
        while True:
            block = f_in.read(16)
            if len(block) == 0:
                break
            ciphertext = cipher_aes.encrypt(block)
            f_out.write(ciphertext)
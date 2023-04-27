from Crypto.Cipher import AES

# Đọc IV từ file đã được mã hóa
with open('Game.enc', 'rb') as f_in:
    iv = f_in.read(16)

# Đọc khóa từ file text.txt
with open('text.txt', 'r') as f_key:
    key_hex = f_key.read().strip()
    key = bytes.fromhex(key_hex)

# Tạo đối tượng AES cipher với khóa và IV đã đọc
cipher_aes = AES.new(key, AES.MODE_CFB, iv)

# Giải mã dữ liệu từ file đã được mã hóa
with open('Game.enc', 'rb') as f_in:
    # Bỏ qua IV
    f_in.read(16)

    # Đọc từng khối dữ liệu 16 byte, giải mã và ghi vào file đầu ra
    with open('Game_decrypted.rar', 'wb') as f_out:
        while True:
            block = f_in.read(16)
            if len(block) == 0:
                break
            plaintext = cipher_aes.decrypt(block)
            f_out.write(plaintext)
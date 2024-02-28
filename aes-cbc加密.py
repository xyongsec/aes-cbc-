from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# 加密函数
def encrypt(text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(text.encode('utf-8'), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

# 解密函数
def decrypt(encrypted_text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher.decrypt(encrypted_text)
    unpadded_text = unpad(decrypted_text, AES.block_size)
    return unpadded_text.decode('utf-8')

# 提供的密钥和初始化向量
key = b'aM7hCmerMs0wdNeZ'
iv = b'oe6uM9C7mEQ861Nb'

# 读取文件内容，逐行加密
with open("username.txt", "r", encoding="utf-8") as file:
    encrypted_lines = []
    for line in file:
        encrypted_line = encrypt(line.rstrip('\n'), key, iv)
        encrypted_lines.append(encrypted_line)

# 将加密后的内容写入新文件（以Base64编码格式）
with open("encrypted_1.txt", "wb") as encrypted_file:
    for encrypted_line in encrypted_lines:
        encrypted_line_base64 = base64.b64encode(encrypted_line)
        zz = base64.b64encode(encrypted_line_base64)
        encrypted_file.write(zz + b'\n')

print("File encrypted and saved as encrypted_1.txt")

# 解密文件内容（为了验证加密和解密的正确性）
with open("encrypted_1.txt", "rb") as encrypted_file:
    decrypted_lines = []
    for encrypted_line_base64 in encrypted_file:
        aa = base64.b64decode(encrypted_line_base64)
        encrypted_line = base64.b64decode(aa.rstrip(b'\n'))
        decrypted_line = decrypt(encrypted_line, key, iv)
        decrypted_lines.append(decrypted_line)

print("Decrypted data:")
for line in decrypted_lines:
    print(line)

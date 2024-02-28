
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
# 提供的加密数据
encrypted_username_b64 = "UTBTNVNLQXVzZWVTSGZqRjhWNGg2Zz09"
encrypted_password_b64 = "ZENyMXJlc1ZBL1E2UHJTTVlYdHlmYVpsNzFBSW94WUdYZ0dFRjNLb1V4eFgxWUoxMjBENDl6SzJ4ZU54YXorRg=="

# BASE64 解码用户信息和密码
encrypted_username = base64.b64decode(encrypted_username_b64)
encrypted_password = base64.b64decode(encrypted_password_b64)
# 提供的加密数据


# 提供的密钥和初始化向量
key = b'aM7hCmerMs0wdNeZ'
iv = b'oe6uM9C7mEQ861Nb'

# 用base64解码来获得加密的字节数据
encrypted_password = base64.b64decode(encrypted_password)
encrypted_username = base64.b64decode(encrypted_username)


# 创建一个新的AES cipher对象
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher1 = AES.new(key, AES.MODE_CBC, iv)

# 解密数据并去除PKCS7填充
try:
    decrypted_password = unpad(cipher.decrypt(encrypted_password), AES.block_size)
    decrypted_username = unpad(cipher1.decrypt(encrypted_username), AES.block_size)
except (ValueError, KeyError) as e:
    # 打印错误信息，比如填充不正确
    print(f"An error occurred: {e}")
else:
    # 如果没有抛出错误，则打印解密结果
    print("Decrypted data:", decrypted_username.decode('utf-8'))
    print("Decrypted data:", decrypted_password.decode('utf-8'))

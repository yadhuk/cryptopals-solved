from Crypto.Cipher import AES
import binascii

cipher = AES.new(b"YELLOW SUBMARINE", AES.MODE_ECB)
lines = b""
with open("7.txt") as file:
     lines += (cipher.decrypt(binascii.a2b_base64(file.read())))

print (lines.decode())
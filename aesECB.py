from Crypto.Cipher import AES
import binascii

# IMPLEMENTED AES-ECB MODE

key = "YELLOW SUBMARINE"

def pad(pt):
    if len(pt) % 16 == 0:
        pt += chr(16) * 16
    elif len(pt) < 16:
        pt += chr((16-len(pt))) * (16-len(pt))
    else:
        pt += chr((16 - (len(pt) % 16))) * (16 - (len(pt) % 16) )
    print (len(pt))
    return pt

def encrypt(pt):
    cipher = AES.new(key , AES.MODE_ECB)
    pt = pad(pt)
    return cipher.encrypt(pt)

def unpad (ct):
    return (ct [:ord(ct[-1])])

def decrypt(ct):
    cipher = AES.new(key, AES.MODE_ECB)
    ct = unpad(ct)
    return cipher.decrypt(ct)

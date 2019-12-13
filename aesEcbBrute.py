import binascii
from Crypto.Cipher import AES

key = "YELLOW SUBMARINE-"

def pad(pt):
    if len(pt) % 16 == 0:
        pt += chr(16) * 16
    elif len(pt) < 16:
        pt += chr((16-len(pt))) * (16-len(pt))
    else:
        pt += chr((16 - (len(pt) % 16))) * (16 - (len(pt) % 16) )
    return pt

def encrypt(pt):
    cipher = AES.new(key, AES.MODE_ECB)
    secret = ''
    pt = pad(pt + str(binascii.a2b_base64(secret)))
    return cipher.encrypt(pt)

def keyLen():
    testString = ""
    defaultLength = len(encrypt(testString))
    count = 0
    while True:
        testString+='A'
        l = len(encrypt(testString))
        count += 1
        if defaultLength != l:
            return defaultLength-count

def exploit():
    len = keyLen()
    print ("Key Length: ", len)
    foundKey = ""

    for i in range(15, 0, -1):
        mainStr = "A" * i 
        encryptedMain = encrypt(mainStr)[:16]

        for j in range(0,200):
            currentEnc = encrypt( mainStr  + foundKey + chr(j) )[:16]
            if currentEnc == encryptedMain:
                foundKey += chr(j)
                break
    return (foundKey)


print (exploit())


import binascii

# REPEATING KEY CIPHER

plainText = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

key = 'ICE'*len(plainText)
cipherText = b''

for p,k in zip(key, plainText):
   cipherText += bytes([ord(p) ^ ord(k)])

cipherText = binascii.b2a_hex(cipherText)
print (cipherText)



import chall3_modular as xor
import string

# DETECT SINGLE CHAR XOR
file = open("lines.txt")
dct = {}
for line in file:
    cipherText = bytes.fromhex(line[:-1])
    for i in range(1,256):
        xorStr = xor.doXOR(cipherText, i)
        xorScore = xor.score(xorStr)
        if xorScore > 1.1 and xorScore < 1.3:
            dct[chr(i)] = [str(xorScore)[:3], xorStr]
dct = sorted(dct.items(), key=lambda el:el[1], reverse=True)
for ch in list(dct):
    print (ch[1][1])


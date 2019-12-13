import string

fq = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
   'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def process(cipher):
    cipher = bytes.fromhex(cipher)
    dct = {}
    plain = b""

    for j in range(65,122):
        plain = b""
        for i in cipher:
            plain+=(bytes([i ^ j]))
        stri = (str(bytes(plain))[2:-1]).lower()
        score = 0
        for ch in stri:
            if ch in string.ascii_lowercase and (chr(j) in string.ascii_letters):
                score+=fq.get(ch)
        dct[chr(j)]= score

    x = dict(reversed(sorted(dct.items(), key=lambda kv: kv[1])))

    for ch in list(x)[0:10]:
        plain = b""
        print (ch, '|' , str(x[ch])[:5], '| ' , end="")
        for i in cipher:
            plain += (bytes([i ^ ord(ch)]))
        print (str(plain)[2:])

 if __name__ == "__main__":
    process("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

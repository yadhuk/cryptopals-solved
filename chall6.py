binary_seq_1, binary_seq_2 = b'this is a test', b'wokka wokka!!!'
count = 0
for b1, b2 in zip(binary_seq_1, binary_seq_2):
    diff = b1 ^ b2
    for i in (bin(diff)):
        if i == '1':
            count+=1

from binascii import hexlify,unhexlify
from hashlib import md5
from random import Random
from randcrack import RandCrack
from sympy import Predicate
from Crypto.Util.number import long_to_bytes,bytes_to_long
XOR = lambda s1 ,s2 : bytes([x1 ^ x2 for x1 ,x2 in zip(s1 , s2)])

def decrypt(cipher , plain):
    tmp = md5(plain).digest()
    c = unhexlify(cipher)
    key = XOR(c,tmp)
    print(key,len(key))
    return key

flag = "npuctf{"
tail = "}"



with open('cipher.txt','r') as f:
    cipher = f.read()
    # 拆分为26个
    key = []
    Predicate_key = []
    rc = RandCrack()
    for i in range(8):
        c = cipher[i*32:i*32+32]
        key.append(decrypt(c,flag[i].encode()))
        rc.submit(bytes_to_long(key[i]))
        Predicate_key.append(rc.predict_getrandbits(32*19))
        if decrypt(cipher[:-32],'}'.encode()) == Predicate_key[:-16]:
            print(Predicate_key)
            print("Done")
            break;





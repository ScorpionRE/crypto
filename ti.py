import base64
import binascii
import codecs
import itertools

import gmpy2
import libnum
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long
from sympy import nthroot_mod
from sympy.ntheory.modular import crt


from libnum import*
import struct
import binascii

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import random
from Crypto.Util.number import *

# from libnum import*
# import struct
# import binascii
#
#从公钥文件中获取n、e的值
with open("pubkey.pem",'rb') as f:
    pub = RSA.importKey(f.read())
    n = pub.n
    e = pub.e
    print(n,'\n',e)


#解密文件

key_info = RSA.construct((n, e, int(d), p, q))
key = RSA.importKey(key_info.exportKey())
key = PKCS1_OAEP.new(key)
f = open('flag.enc', 'r').read()

flag = key.decrypt(f)
print(flag)










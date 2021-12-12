#从公钥文件中获取n、e的值
import base64

import gmpy2

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import rsa

#从公钥文件中获取n、e的值
from Crypto.Util.number import bytes_to_long, long_to_bytes

with open("pubkey.pem",'rb') as f:
    pub = RSA.importKey(f.read())
    n = pub.n
    e = pub.e
    print(n,'\n',e)

p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239
phi = (p-1)*(q-1)
print(gmpy2.gcd(e,phi))
#d = gmpy2.invert(e,phi)
#解密文件

# key_info = RSA.construct((n, e, int(d), p, q))
# key = RSA.importKey(key_info.exportKey())
# key = PKCS1_OAEP.new(key)
f = open('flag.enc', 'rb').read()
f = bytes_to_long(f)
print(f)
m = gmpy2.iroot(f,2)
print(m)
print(hex(m[0]))
print(long_to_bytes(m[0]))
#c = base64.b64decode(f)
#


# Rsa=rsa.PrivateKey(int(n1), int(e1), int(d1), int(p), int(q1))
# with open('flag_encry1','rb') as f:
#      cipher1=f.read()
#      print(rsa.decrypt(cipher1, Rsa))
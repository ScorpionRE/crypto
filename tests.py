import base64
import codecs
import string

from Crypto.Util.number import bytes_to_long

import codes
import Rsa

n = 0xC2636AE5C3D8E43FFB97AB09028F1AAC6C0BF6CD3D70EBCA281BFFE97FBE30DD
e = 65537
p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239
n,e = Rsa.get_ne("pubkey.pem")

with open("flag.enc",'rb') as f:
    f = f.read()
    print(f)
    c = bytes_to_long(f)
    print(c)
    #c = string.atoi(f,16)
    Rsa.little_e(e,c,n)
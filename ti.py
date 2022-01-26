import base64
import codecs
import sys
import Rsa

# import this
from Crypto.Util.number import long_to_bytes
from pwn import xor

import base64
import otp
cipher = base64.b64decode('ExcKewcfFkdOWEYpISUbFSseXX8wQB0Le3kDByMcLQQ=')
plain = 'YQAM4hBv435OgKZVxzdLSuJq5LSRqFcL'
passwd = base64.b64decode('CzVrT1wCdFoUBARGMgYgN3McVkFDQzIINxUjPD8qIi0=')
key = ''
result = ''
for i in range(len(plain)):
    key = xor(plain,cipher)
print(key)
for i in range(len(key)):
    result = xor(key,passwd)

print(result)

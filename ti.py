import base64
import codecs
import sys
# import this
from Crypto.Util.number import long_to_bytes
import pwntools
if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2  = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

def xor(a,b):
    m = ""
    for i in a:
        m+=chr(ord(i)^b)
    print(m)
    return m
print("Here is your flag:")

print(xor(ords,m))

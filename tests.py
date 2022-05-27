from Crypto.Util.number import *
import sys
import hashlib
import json
fp=open("flag.txt.enc","rb")
b=fp.read()
fp.close()
data = {
            "filename": 'flag.txt',
            "hash": ' ',
            "plaintext":' '
        }
outbuf = json.dumps(data, sort_keys=True, indent=4)
s=""
for i in range(min(len(outbuf),len(b))):
    s+=chr(b[i]^ord(outbuf[i]))
print(s)

key=b'n0t4=l4g'
ans=''
for i in range(len(b)):
    ans+=chr(b[i]^key[i%len(key)])
print(ans)

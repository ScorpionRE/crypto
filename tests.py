s=b'<?xml version="1.0" encoding="UTF-8"?>'
f=open('flag.svg.enc','rb').read()
import hashlib
import struct
sha0=bytes()
x1=bytes(a^b for a,b in zip(s[:32],f[:32]))
sha0+=x1
temp=1
for i in range(len(f)):
    x1=hashlib.sha256(x1+struct.pack('<I',temp)).digest()
    sha0+=x1
    temp+=1
flag=bytes(a^b for a,b in zip(sha0,f))
print(flag)

#CTF{but_even_I_couldnt_break_IT}


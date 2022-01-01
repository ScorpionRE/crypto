from itertools import cycle
import codecs, numpy as np
import Crypto.Util.strxor as xo
from Crypto.Util.number import bytes_to_long

from codes import cipher

#前一部分得到key
c = 0x72472201E3C0AC877A27C18729749FDA185C1DF902500AEB425C5B6A53574B4A00508546094A90A2F1547780FD401E8C2983A70F22931F0BCC0EBE6EC83B1284BF2023AEBE59B1CBD2D9C395E9C76D42DF65C470C23C92E65F66504F3025B5F660E772096A172CDD
#c = cipher.decode(c,'hex')
c = codecs.decode(c,'hex')
with open('Plain.txt','r') as f:
    s = f.read()
m = ""
for i in range(8):
    m += chr(ord(s[i])^ord(c[i]))

print(m)

#计算lfsr密钥流

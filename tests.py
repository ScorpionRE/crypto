from binascii import unhexlify
from sympy.ntheory.modular import crt
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long,long_to_bytes
import gmpy2 


with open('new.txt','r') as f:
    news = [unhexlify(line.strip()) for line in f ]
    #print(cipher)
with open('key','r') as k:
    keys = [unhexlify(line.strip()) for line in k]
    #print(key)

with open('product','r') as n:
    n = [int(line.strip()) for line in n]
    #print(n)

# Get states_2
states_2 = []
iv = b'\x00' * 16
for i in range(48, 72):
    cipher = AES.new(keys[i], AES.MODE_CBC, iv)
    states_2.append(cipher.decrypt(news[i-48]))

# Get states_1 (c)
states_1 = []
for i in range(24, 48):
    cipher = AES.new(keys[i], AES.MODE_CBC, iv)
    states_1.append(cipher.decrypt(states_2[i-24]))
c = [bytes_to_long(x) for x in states_1]
#print(c)
# 广播攻击
M = crt(n,c)[0]
print(M)
m = gmpy2.iroot(M,17)[0]
print(long_to_bytes(m))


def mul(x):
    a = 0
    for i in bin(x)[2:]:
        a = a << 1
        if (int(i)):
            a = a ^ x
        if a >> 256:
            a = a ^ 0x10000000000000000000000000000000000000000000000000000000000000223
    return a

# 有限域计算
def dec2(m):
    while True:
        m = mul(m)
        if b"flag" in long_to_bytes(m):
            print(long_to_bytes(m))
            break
dec2(m)
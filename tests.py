# from binascii import hexlify,unhexlify
# from hashlib import md5
# from random import Random
# from randcrack import RandCrack
# from sympy import Predicate
# from Crypto.Util.number import long_to_bytes,bytes_to_long
# XOR = lambda s1 ,s2 : bytes([x1 ^ x2 for x1 ,x2 in zip(s1 , s2)])

# def decrypt(cipher , plain):
#     tmp = md5(plain).digest()
#     c = unhexlify(cipher)
#     key = XOR(c,tmp)
#     print(key,len(key))
#     return key

# flag = "npuctf{"
# tail = "}"



# with open('cipher.txt','r') as f:
#     cipher = f.read()
#     # 拆分为26个
#     key = []
#     Predicate_key = []
#     rc = RandCrack()
#     for i in range(8):
#         c = cipher[i*32:i*32+32]
#         key.append(decrypt(c,flag[i].encode()))
#         rc.submit(bytes_to_long(key[i]))
#         Predicate_key.append(rc.predict_getrandbits(32*19))
#         if decrypt(cipher[:-32],'}'.encode()) == Predicate_key[:-16]:
#             print(Predicate_key)
#             print("Done")
#             break;


from binascii import hexlify, unhexlify
from hashlib import md5
from Crypto.Util.number import bytes_to_long,long_to_bytes
from gmpy2 import invert
 
XOR = lambda s1, s2: bytes([x1 ^ x2 for x1, x2 in zip(s1, s2)])
 
 
def inverse_right(res, shift, mask=0xffffffff, bits=32):
    tmp = res
    for i in range(bits // shift):
        tmp = res ^ tmp >> shift & mask
    return tmp
 
 
def inverse_left(res, shift, mask=0xffffffff, bits=32):
    tmp = res
    for i in range(bits // shift):
        tmp = res ^ tmp << shift & mask
    return tmp
 
 
# 逆srand
def recover(last):
    n = 1 << 32
    inv = invert(1812433253, n)
    for i in range(103, -1, -1):
        last = ((last + i) * inv) % n
        last = inverse_right(last, 27)
    return last
 
 
# 逆next
def Last(tmp):
    tmp = inverse_right(tmp, 18, 0x34adf670)
    tmp = inverse_left(tmp, 15, 0xefc65400)
    tmp = inverse_left(tmp, 7, 0x9ddf4680)
    tmp = inverse_right(tmp, 11)
    return tmp
 
 
# 逆state0
cip = b'cef4876036ee8b55aa59bca043725bf3'
assert len(cip) == 32
cip = unhexlify(cip)
tmp = md5('n'.encode()).digest()
key = XOR(tmp, cip)
newstate0 = Last(bytes_to_long(key[:4]))
print(newstate0)
# 逆state103
key = unhexlify(b'b223dde6450ba6198e90e14de107aaf2')
tmp = md5('}'.encode()).digest()
key = XOR(tmp, key)
newstate103 = Last(bytes_to_long(key[-4:]))
print(newstate103)
# 得到oldstate104的两种情况
y_1 = newstate103 ^ newstate0
print(bin(y_1))
if newstate103 >> 31 == 1:
    y = (y_1 ^ 0x9908b0df) << 1 + 1
else:
    y = y_1 << 1
print(bin(y))
oldstate104_1 = (y << 1) >> 1
oldstate104_2 = oldstate104_1 + (1 << 31)
# 验证哪种是对的 这部分有点丑hhh
n = 1 << 32
inv = invert(1812433253, n)
t1 = oldstate104_1
t1 = ((t1 + 103) * inv) % n
t1 = inverse_right(t1, 27)
t2 = oldstate104_1
t2 = ((t2 + 103) * inv) % n
t2 = inverse_right(t2, 27)
oldstate104=0
if t1 & 0x80000000 == y & 0x80000000:
    if t2 & 0x80000000 == y & 0x80000000:
        print('both are right')
    else:
        oldstate104=oldstate104_1
else:
    oldstate104=oldstate104_2
#恢复seed
seed=recover(oldstate104)
print(seed)
 
class mt73991:
    def __init__(self, seed):
        self.state = [seed] + [0] * 232
        self.flag = 0
        self.srand()
        self.generate()
 
    def srand(self):
        for i in range(232):
            self.state[i + 1] = 1812433253 * (self.state[i] ^ (self.state[i] >> 27)) - i
            self.state[i + 1] &= 0xffffffff
 
    def generate(self):
        for i in range(233):
            y = (self.state[i] & 0x80000000) | (self.state[(i + 1) % 233] & 0x7fffffff)
            temp = y >> 1
            temp ^= self.state[(i + 130) % 233]
            if y & 1:
                temp ^= 0x9908f23f
            self.state[i] = temp
 
    def getramdanbits(self):
        if self.flag == 233:
            self.generate()
            self.flag = 0
        #原题的代码下面的这行没int转换
        bits = int(self.Next(self.state[self.flag])).to_bytes(4, 'big')
        self.flag += 1
        return bits
 
    def Next(self, tmp):
        tmp ^= (tmp >> 11)
        tmp ^= (tmp << 7) & 0x9ddf4680
        tmp ^= (tmp << 15) & 0xefc65400
        tmp ^= (tmp >> 18) & 0x34adf670
        return tmp
random = mt73991(seed)
#储存可见字符的md5
S=b''
for i in range(0x20,0x7f):
    S+=long_to_bytes(i)
S_list = []
for i in S:
    tmp = md5(chr(i).encode()).digest()
    S_list.append(tmp)
def decrypt(key, cipher):
    tmp = XOR(key, unhexlify(cipher))
    for i in range(len(S)):
        if S_list[i] == tmp:
            return long_to_bytes(S[i])
    return b''
#开始解密
c = open('./cipher.txt', 'rb').read()
flag = b''
for i in range(len(c)//32):
    key = b''.join([random.getramdanbits() for _ in range(4)])
    cipher = c[i*32:(i+1)*32]
    flag += decrypt(key,cipher)
print(flag)
#reference https://am473ur.com/writeup-for-crypto-problems-in-npuctf-2020/#mersenne_twister
#reference https://0xdktb.top/2020/04/19/WriteUp-NPUCTF-Crypto/



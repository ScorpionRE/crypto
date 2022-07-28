# AES
from Crypto.Cipher import AES
import os
from gmpy2 import *
from Crypto.Util.number import *

# xor = 91144196586662942563895769614300232343026691029427747065707381728622849079757
# enc_flag = b'\x8c-\xcd\xde\xa7\xe9\x7f.b\x8aKs\xf1\xba\xc75\xc4d\x13\x07\xac\xa4&\xd6\x91\xfe\xf3\x14\x10|\xf8p'
# out = long_to_bytes(xor)
# print(out)
# key = out[:16] * 2
# print(key)
# iv = bytes_to_long(key[16:]) ^ bytes_to_long(out[16:])
# print(iv)
# iv = long_to_bytes(iv)
# print(iv)
# aes = AES.new(key, AES.MODE_CBC, iv)
# flag = aes.decrypt(enc_flag)
# print(flag)
# !/usr/bin/env python
# coding=utf-8

#ECB模式攻击
# import conn
# import os
#
# number = 30 + 16
# mess = "hello, 111111111111, your mission's flag is: moeflag{"
# ans = ""
# while (number >= 0):
#     found = False
#     conn.remote("175.178.248.28", 10086)
#     conn.reads()
#     mess = "1" * number
#     conn.sends("1\n")
#     conn.sends(mess)
#     # print("发送 " + mess)
#     initialdata = conn.reads()
#     # print("原始 "+initialdata)
#     blockdata = initialdata[0:128 + 32]
#     # print("前端 \n"+blockdata)
#     # print(initialdata)
#     # print("----------")
#     array = "mqmwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789{}_-~!@#$%^&*()-=+[]?><'|,./`\"m"  # 枚举的集合
#
#     for i in array:
#         conn.reads()
#         # print("尝试 "+i)
#         mess = "hello, " + "1" * number + ", your mission's flag is: " + ans + i
#         conn.sends(mess)
#         data = conn.reads()
#         # print(data)
#
#         # print data
#         if data[0:128 + 32] == blockdata:
#             found = True
#             print("发现 " + i)
#             ans += i
#             number = number - 1
#             if i == "}":
#                 number = -1
#                 print("答案:" + ans)
#                 os.system("pause")
#                 # message=message+i
#             break
#     conn.close()
#     if not found:
#         print("没有找到~~")
#         os.system("pause")
# print(ans)

#DES
# import pyDes
# import base64
# from Crypto.Util.number import *
# while True:
#     deskey = os.urandom(8)
#     DES = pyDes.des(deskey)
#     DES.Kn[10] =  [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
#     # cipher_list = base64.b64encode(DES.encrypt(flag))
#     with open("cipher",'rb') as f:
#         k = f.read()
#
#     print(k)
#     flag = DES.decrypt(k)
#     print(flag.decode())
#     print(flag)

# DES,Kn泄露
from symmetric.DES import *
from itertools import product

guess_8bit = list(product(range(2), repeat=8))
not_in_PC2 = [9,18,22,25,35,38,43,54]

def re_PC2(sbkey):
    # 48-bit -> 56-bit
    res = [0]*56
    for i in range(len(sbkey)):
        res[PC_2_table[i]-1] = sbkey[i]
    return res # ok
def guess_CrDr(subkey,t):
    res = re_PC2(subkey)
    for i in range(8):
        res[not_in_PC2[i]-1] = guess_8bit[t][i]
    return res

def guess_allsubkey(roundkey,r,t):
    subkey = [[]]*16
    subkey[r] = roundkey
    CrDr = guess_CrDr(roundkey,t)
    Cr,Dr = CrDr[:28],CrDr[28:]
    for i in range(r+1,r+16):
        Cr,Dr = LR(Cr,Dr,i%16)
        subkey[i%16] = PC_2(Cr+Dr)
    return subkey

def des_enc(c,k):
    assert len(c) % 8 == 0
    res = b''
    for i in range(0,len(c),8):
        res += DES_enc(c[i:i+8], k)
    return res

def try_des(cipher,roundkey):
    for t in range(256): #2^8
        allkey = guess_allsubkey(roundkey,10,t)
        plain = des_enc(cipher,allkey[::-1])
        if plain.startswith(b'NCTF'):
            print(plain)





if __name__ == "__main__":
    with open('cipher','rb') as f:
        flag_enc = f.read()

    k10 = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    try_des(flag_enc,k10)
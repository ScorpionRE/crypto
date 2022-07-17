import hashlib

#m="38e4c352809e150186920aac37190cbc"
# flag=""
# for j in range(0,26):
#     flag=""
#     for i in range(len(b)):
#         flag+=chr(int(b[i]))
#     print(flag)

# flag="flag{www_shiyanbar_com_is_very_good_"
#
# for x in range(21,127):
#     for y in range(21,127):
#         for z in range(21,127):
#             for q in range(21,127):
#                 w=hashlib.sha256(str(flag + chr(x) + chr(y) + chr(z) + chr(q) + "}")).encode("utf-8"))
#                 w0=w.hexdigest()
#
#                 if(w0==m):
#                     print(flag+chr(x)+chr(y)+chr(z)+chr(q)+"}")
#                     break

#md5爆破
# s = hashlib.md5('525520'.encode('utf8')).hexdigest()
# print(s)
#print hashlib.md5(s).hexdigest().upper()
# k = 'TASC?O3RJMV?WDJKX?ZM'                    #要还原的明文
# for i in range(26):
#     temp1 = k.replace('?',str(chr(65+i)),1)
#     for j in range(26):
#         temp2 = temp1.replace('?',chr(65+j),1)
#         for n in range(26):
#             temp3 = temp2.replace('?',chr(65+n),1)
#             s = hashlib.md5(temp3.encode('utf8')).hexdigest().upper()#注意大小写
#             if s[:4] == 'E903':    #检查元素
#                 print (s)       #输出密文

#三位爆破
# flag="de54015e59c7b"
# m = "69eaae8b278cf1deb43c379be05c06447f37c94090234af2751d3dab1266e36e"
# for x in range(21,127):
#     for y in range(21,127):
#         for z in range(21,127):
#
#             w=hashlib.sha256(str(flag + chr(x) + chr(y) + chr(z)  ).encode("utf-8"))
#             w0=w.hexdigest()
#
#             if(w0==m):
#                 print(flag + chr(x)+chr(y)+chr(z) )
#                 break


#sha256爆破
def brute_sha256(flag,m):
    for x in range(21,127):
        for y in range(21,127):
            for z in range(21,127):
                for q in range(21,127):
                    w=hashlib.sha256(str( chr(x) + chr(y) + chr(z) + chr(q) + flag ).encode("utf-8"))
                    w0=w.hexdigest()

                    if(w0==m):
                        print( chr(x)+chr(y)+chr(z) + chr(q) + flag)
                        return chr(x)+chr(y)+chr(z)+chr(q)

from Crypto.Util.number import *
import os
def brute_urandom_sha256(prefix,hash):
    pre = long_to_bytes(prefix)
    for x in range(0,255):
        for y in range(0,255):
            for z in range(0,255):
                str = pre + bytes(chr(x),encoding = 'utf-8') +bytes(chr(y),encoding = 'utf-8') + bytes(chr(z),encoding = 'utf-8')
                w = hashlib.sha256(str)
                w0 = w.hexdigest()

                if(w0 == hash):
                    print(pre + bytes(chr(x),encoding = 'utf-8') +bytes(chr(y),encoding = 'utf-8') + bytes(chr(z),encoding = 'utf-8'))
                    return chr(x) + chr(y) + chr(z)

flag="P1rBPgWVKeFo6bo1"
hash = "af494c242b3f0fc89304851e6333cd67b2a66971af318c1cbef4e63cc3704817"

# brute_sha256(flag,m)
# brute_urandom_sha256(0x88b204570b,'8eab34f25ad44b972393295e3757d1ebcdb977055483a3cdab38ce8bb768e439')
print(hex(9849940106913545081))
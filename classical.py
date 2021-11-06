#古典密码
#简单移位密码
import base64
import binascii
import codecs
'''
m,k
以k的长度l切分m
明文字符位置1234
密文字符位置3124（如把第一个字符放到第三个去）
'''
#
# def shift_encrypt(m,k):
#     l = len(k)
#     c = ""
#     for i in range(0,len(m),l):
#         tmp_c = [""]*l
#         if i + 1 > len(m):
#             tmp_m = m[i:]
#         else:
#             tmp_m = m[i:i+l]
#         for kidx in range(len(tmp_m)):
#             tmp_c[int(k[kidx]) - 1] = tmp_m[kidx]
#         c += "".join(tmp_c)
#     return c
#
# def shift_decrypt(c,k):
#     l = len(k)
#     m = ""
#     for i in range(0,len(c),l):
#         tmp_m = [""] * l
#         if i + l >= len(c):
#             tmp_c = c[i:]
#             use = []
#             for kidx in range(len(tmp_c)):
#                 use.append(int(k[kidx]) - 1)
#             use.sort()
#             for kidx in range(len(tmp_c)):
#                 tmp_m[kidx] = tmp_c[use.index(int(k[kidx])-1)]
#
#         else:
#             tmp_c = c[i:i+l]
#             for kidx in range(len(tmp_c)):
#                 tmp_m[kidx] = tmp_c[int(k[kidx]) - 1]
#
#         m += "".join(tmp_m)
#
#     return m
#
# #云影密码
#
# def c01248_decode(c):
#     l=c.split("0")
#     origin = "abcdefghijklmnopqrstuvwxyz"
#     r = ""
#     for i in l:
#         tmp = 0
#         for num in i:
#             tmp += int(num)
#             r += origin[tmp-1]
#     return r

#xor
a = 'lovelovelovelovelovelovelovelove'
b = [0x0A,0x03,0x17,0x02,0x56,0x01,0x15,0x11,0x0A,0x14,0x0E,0x0A,0x1E,0x30,0x0E,0x0A,0x1E,0x30,0x0E,0x0A,0x1E,0x30,0x14,0x0C,0x19,0x0D,0x1F,0x10,0x0E,0x06,0x03,0x00]

c = ''
for i in range(len(a)):
    c += chr(ord(a[i])^b[i])
print(c)
#"凯撒密码解密")
#密文
# str = 'R5UALCUVJDCGD63RQISZTBOSO54JVBORP5SAT2OEQCWY6CGEO53Z67L'
# #密钥(平移位数)
# m = ''
# for my in range(1,26):
#     print("密钥",my)
#     for i in str:
#       mw = ord(i)
#       if (64 < mw < 91):#大写字母
#         jm = mw + my
#         if jm > 90:
#               jm = (mw - 26) + my
#               m += chr(jm)
#           #m.join(chr(jm))
#           #print(chr(jm), end='')
#         else:
#             m += chr(jm)
#           #print(chr(jm), end='')
#       elif (96 < mw < 123):#小写字母
#         jm = mw + my
#         if jm > 122:
#             jm = (mw - 26) + my
#             m += chr(jm)
#           #print(chr(jm), end='')
#         else:
#             m += chr(jm)
#           #print(chr(jm), end='')
#       else:#数字和特殊字符不做修改
#         jm = mw + 0
#         m += chr(jm)
#         #print(chr(jm), end='')
#     print(m)
#     try:
#         print(base64.b32decode(m))
#     except binascii.Error:
#         missing_padding = 2 - len(m) % 2  #base64为4
#         if missing_padding:
#             m += '=' * missing_padding
#         print(base64.b32decode(m))
#     m = ''
#



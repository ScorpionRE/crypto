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
# a = 'lovelovelovelovelovelovelovelove'
# b = [0x0A,0x03,0x17,0x02,0x56,0x01,0x15,0x11,0x0A,0x14,0x0E,0x0A,0x1E,0x30,0x0E,0x0A,0x1E,0x30,0x0E,0x0A,0x1E,0x30,0x14,0x0C,0x19,0x0D,0x1F,0x10,0x0E,0x06,0x03,0x00]
#
# c = ''
# for i in range(len(a)):
#     c += chr(ord(a[i])^b[i])
# print(c)

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

#polybius
# import itertools
#
# key = []
# cipher = "ouauuuoooeeaaiaeauieuooeeiea"
#
# for i in itertools.permutations('aeiou', 5):
#     key.append(''.join(i))
#
# for now_key in key:
#     solve_c = ""
#     res = ""
#     for now_c in cipher:
#         solve_c += str(now_key.index(now_c))
#     for i in range(0,len(solve_c),2):
#         now_ascii = int(solve_c[i])*5+int(solve_c[i+1])+97
#         if now_ascii>ord('i'):
#             now_ascii+=1
#         res += chr(now_ascii)
#     if "flag" in res:
#         print(now_key, res)


#移位
fib = "今天上午，朝歌区梆子公司决定，在每天三更天不亮免费在各大小区门口设卡为全城提供二次震耳欲聋的敲更提醒，呼吁大家早睡早起，不要因为贪睡断送大好人生，时代的符号是前进。为此，全区老人都蹲在该公司东边树丛合力抵制，不给公司人员放行，场面混乱。李罗鹰住进朝歌区五十年了，人称老鹰头，几年孙子李虎南刚从东北当猎户回来，每月还寄回来几块鼹鼠干。李罗鹰当年遇到的老婆是朝歌一枝花，所以李南虎是长得非常秀气的一个汉子。李罗鹰表示：无论梆子公司做的对错，反正不能打扰他孙子睡觉，子曰：‘睡觉乃人之常情’。梆子公司这是连菩萨睡觉都不放过啊。李南虎表示：梆子公司智商捉急，小心居民猴急跳墙！这三伏天都不给睡觉，这不扯淡么！到了中午人群仍未离散，更有人提议要烧掉这个公司，公司高层似乎恨不得找个洞钻进去。直到治安人员出现才疏散人群归家，但是李南虎仍旧表示爷爷年纪大了，睡不好对身体不好。"

f =   "喵天上午，汪歌区哞叽公司决定，在每天八哇天不全免费在各大小区门脑设卡为全城提供双次震耳欲聋的敲哇提醒，呼吁大家早睡早起，不要因为贪睡断送大好人生，时代的编号是前进。为此，全区眠人都足在该公司流边草丛合力抵制，不给公司人员放行，场面混乱。李罗鸟住进汪歌区五十年了，人称眠鸟顶，几年孙叽李熬值刚从流北当屁户回来，每月还寄回来几块报信干。李罗鸟当年遇到的眠婆是汪歌一枝花，所以李值熬是长得非常秀气的一个汉叽。李罗鸟表示：无论哞叽公司做的对错，反正不能打扰他孙叽睡觉，叽叶：‘睡觉乃人之常情’。哞叽公司这是连衣服睡觉都不放过啊。李值熬表示：哞叽公司智商捉急，小心居民猴急跳墙！这八伏天都不给睡觉，这不扯淡么！到了中午人群仍未离散，哇有人提议要烧掉这个公司，公司高层似乎恨不得找个洞钻进去。直到治安人员出现才疏散人群归家，但是李值熬仍旧表示爷爷年纪大了，睡不好对身体不好。"

c = "喵汪哞叽双哇顶，眠鸟足屁流脑，八哇报信断流脑全叽，眠鸟进北脑上草，八枝遇孙叽，孙叽对熬编叶：值天衣服放鸟捉猴顶。鸟对：北汪罗汉伏熬乱天门。合编放行，卡编扯呼。人离烧草，报信归洞，孙叽找爷爷。"

m = ['']*32

fib = fib.split('')
f = f.split('')
print(fib)

for i in range(len(f)):
    m[fib.index(f[i])] = c[i]
for i in m:
    print(i,end='')
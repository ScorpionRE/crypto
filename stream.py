import codecs
import string
from itertools import cycle

# break repeating-key [xorz]

##计算a,b之间的汉明距离res
# def haming(a,b):
#     res = 0
#     for x,y in zip(a,b): #打包为元组的列表，个数与最短的一致
#         res += bin(ord(x)^ord(y)).count(1) #异或之后计算1的数量即两个字母之间的汉明距离
#     #print(res)
#     return res
#
#
# def break_single_key_xor(text):
#     key = 0
#     possible_space = 0
#     max_possible = 0
#     letters = string.ascii_letters # 所有的大小写英文字母
#     for a in range(0,len(text)):
#         maxpossible = 0
#         for b in range(0,len(text)):
#             if(a == b):
#                 continue
#             c = ord(text[a])^ord(text[b])
#             if chr(c) not in letters and c!=0:
#                 continue
#             maxpossible += 1
#         if maxpossible>max_possible:
#             max_possible = maxpossible
#             possible_space = a
#     key = ord(text[possible_space])^0x20
#     return chr(key)
#
# cipher = '49380d773440222d1b421b3060380c3f403c3844791b202651306721135b6229294a3c3222357e766b2f15561b35305e3c3b670e49382c295c6c170553577d3a2b791470406318315d753f03637f2b614a4f2e1c4f21027e227a4122757b446037786a7b0e37635024246d60136f7802543e4d36265c3e035a725c6322700d626b345d1d6464283a016f35714d434124281b607d315f66212d671428026a4f4f79657e34153f3467097e4e135f187a21767f02125b375563517a3742597b6c394e78742c4a725069606576777c314429264f6e330d7530453f22537f5e3034560d22146831456b1b72725f30676d0d5c71617d48753e26667e2f7a334c731c22630a242c7140457a42324629064441036c7e646208630e745531436b7c51743a36674c4f352a5575407b767a5c747176016c0676386e403a2b42356a727a04662b4446375f36265f3f124b724c6e346544706277641025063420016629225b43432428036f29341a2338627c47650b264c477c653a67043e6766152a485c7f33617264780656537e5468143f305f4537722352303c3d4379043d69797e6f3922527b24536e310d653d4c33696c635474637d0326516f745e610d773340306621105a7361654e3e392970687c2e335f3015677d4b3a724a4659767c2f5b7c16055a126820306c14315d6b59224a27311f747f336f4d5974321a22507b22705a226c6d446a37375761423a2b5c29247163046d7e47032244377508300751727126326f117f7a38670c2b23203d4f27046a5c5e1532601126292f577776606f0c6d0126474b2a73737a41316362146e581d7c1228717664091c'
# salt="WeAreDe1taTeam"
#
# i = 0
# text = ''
# si = cycle(salt)
# while i < 1199:
#   text += chr(int(("0x"+cipher[i:i+2]),16) ^ ord(next(si)))
#   i += 2
# print(text)
#
# normalized_distances = []
#
# for keysize in range(2,40):
#     c1 = text[:keysize]
#     c2 = text[keysize:keysize*2]
#     c3 = text[keysize*2:keysize*3]
#     c4 = text[keysize*3:keysize*4]
#     c5 = text[keysize*4:keysize*5]
#     c6 = text[keysize*5:keysize*6]
#
#     normalized_distance = float(
#         haming(c1,c2)+
#         haming(c2,c3)+
#         haming(c3,c4)+
#         haming(c4,c5)+
#         haming(c5,c6)
#         )/(keysize*5)
#     normalized_distances.append((keysize,normalized_distance))
#
# normalized_distances = sorted(normalized_distances,key=lambda x:x[1])
# print(normalized_distances)
#
# for keysize,_ in normalized_distances[:5]:
#     block_bytes = [[] for _ in range(keysize)] # 列表的列表
#     for i,byte in enumerate(text):
#         block_bytes[i%keysize].append(byte)
#     keys = ''
#     for bbytes in block_bytes:
#         keys += break_single_key_xor(bbytes)
#     key = cycle(keys)
#     plaintext = ''.join(chr(ord(next(key))^ord(p)) for p in text)
#     print("keysize:",keysize)
#     print("key is:",keys)
#     print(plaintext)


# Lfsr

from Crypto.Util.strxor import strxor
import codecs
cip = open('cipher.txt', 'rb').read()
msg = open('Plain.txt', 'rb').read()

print(codecs.encode(strxor(cip, msg)[:8], 'hex'))

key = '0123456789abcdef'
R = int(key, 16)
mask = 0b1101100000000000000000000000000000000000000000000000000000000000


def lfsr(R, mask):
    # 左移1位：保留末尾 63 位，在最后添加一个0
    output = (R << 1) & 0xffffffffffffffff

    # i：保留 R 的前 0、1、3、4位
    i = (R & mask) & 0xffffffffffffffff

    lastbit = 0
    while i != 0:
        lastbit ^= (i & 1)
        i = i >> 1
    # lastbit：统计 i 里面有多少个1, 奇数个则为1, 偶数个则为0

    # output: R 左移1位，再添加 lastbit
    output ^= lastbit
    return (output, lastbit)


cip = open('flag_encode.txt', 'rb').read()
a = ''.join([chr(int(b, 16)) for b in [key[i:i + 2] for i in range(0, len(key), 2)]])

ans = ""

for i in range(len(a)):
    ans += (chr((cip[i] ^ ord(a[i]))))

lent = len(cip)

for i in range(len(a), lent):
    tmp = 0
    for j in range(8):
        (R, out) = lfsr(R, mask)
        tmp = (tmp << 1) ^ out
    ans += (chr(tmp ^ cip[i]))

print(ans)
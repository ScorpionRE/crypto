import base64
#十六进制转ASCII
import codecs


#base64
import re


def base64decode(res):
    missing_padding = 4 - len(res) % 4
    if missing_padding:
        res += '=' * missing_padding
    flag=base64.b64decode(res)
    print(flag)
    return flag
# import base64
# file = open("3.txt",'r')
# file2 = open("flag",'w')
# base = file.read()
# # while(1):
# #     try:
# #         base = base64.b32decode(base).decode()
# #     except:
# #         try:
# #             base = base64.b64decode(base).decode()
# #         except:
#
# base = base64.b16decode(base).decode()
# print(base)  #?输出的和原本的不一样？只有写入文件才是一样的
# file2.write(base)


#曼彻斯特
def bintohex(s1):
    s2 = ''
    s1 = re.findall('.{4}', s1)
    print('每一个hex分隔:', s1)
    for i in s1:
        s2 += str(hex(int(i, 2))).replace('0x', '')

    print('ID:', s2)


def diffmqst(s):
    s1 = ''
    s = re.findall('.{2}', s)
    cc = '01'
    for i in s:
        if i == cc:
            s1 += '0'
        else:
            s1 += '1'
        cc = i  # 差分加上cc = i

    print('差分曼切斯特解码:', s1)
    bintohex(s1)
#将cipher（十六禁止）转换为曼彻斯特编码，0->1表示1
def mcst_011(cipher):
    tmp=''
    for i in range(len(cipher)):
        a=bin(eval('0x'+cipher[i]))[2:].zfill(4)
        tmp=tmp+a[1]+a[3]
    print(tmp)

def mcst_101(cipher):
    tmp = ''
    for i in range(len(cipher)):
        a=bin(eval('0x'+cipher[i]))[2:].zfill(4)
        tmp=tmp+a[0]+a[2]
    print(tmp)

#键盘密码
# strr = "ooo yyy ii w uuu ee uuuu yyy uuuu y w uuu i i rr w i i rr rrr uuuu rrr uuuu t ii uuuu i w u rrr ee www ee yyy eee www w tt ee".split()
# all = {'none1':'','none2':'','w':'abc','e':'def','r':'ghi','t':'jkl','y':'mno','u':'pors','i':'tuv','o':'wxyz'}
# for i in strr:
#     print(all[i[0]][len(i)-1],end="")





#替换base字母表

# dict= "JASGBWcQPRXEFLbCDIlmnHUVKTYZdMovwipatNOefghq56rs34ujkxyz012789+/="
# base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
# cipher='MyLkTaP3FaA7KOWjTmKkVjWjVzKjdeNvTnAjoH9iZOIvTeHbvD=='
# res=''
# for i in range(len(cipher)):
#     for j in range(64):
#         if(dict[j]==cipher[i]):
#             res+=base64_list[j]
# print(res)

#b'BJD{D0_Y0u_kNoW_Th1s_b4se_map}'




#64卦

Table = {
    '乾': 'A',
    '坤': 'B',
    '屯': 'C',
    '蒙': 'D',
    '需': 'E',
    '讼': 'F',
    '师': 'G',
    '比': 'H',
    '小畜': 'I',
    '履': 'J',
    '泰': 'K',
    '否': 'L',
    '同人': 'M',
    '大有': 'N',
    '谦': 'O',
    '豫': 'P',
    '随': 'Q',
    '蛊': 'R',
    '临': 'S',
    '观': 'T',
    '噬嗑': 'U',
    '贲': 'V',
    '剥': 'W',
    '复': 'X',
    '无妄': 'Y',
    '大畜': 'Z',
    '颐': 'a',
    '大过': 'b',
    '坎': 'c',
    '离': 'd',
    '咸': 'e',
    '恒': 'f',
    '遁': 'g',
    '大壮': 'h',
    '晋': 'i',
    '明夷': 'j',
    '家人': 'k',
    '睽': 'l',
    '蹇': 'm',
    '解': 'n',
    '损': 'o',
    '益': 'p',
    '夬': 'q',
    '姤': 'r',
    '萃': 's',
    '升': 't',
    '困': 'u',
    '井': 'v',
    '革': 'w',
    '鼎': 'x',
    '震': 'y',
    '艮': 'z',
    '渐': '1',
    '归妹': '2',
    '丰': '3',
    '旅': '4',
    '巽': '5',
    '兑': '6',
    '涣': '7',
    '节': '8',
    '中孚': '9',
    '小过': '0',
    '既济': '+',
    '未济': '/'

}
#数据在内存中的存储
# from libnum import*
# import struct
# import binascii
#
# s = [72143238992041641000000.000000,77135357178006504000000000000000.000000,1125868345616435400000000.000000,67378029765916820000000.000000,75553486092184703000000000000.000000,4397611913739958700000.000000,76209378028621039000000000000000.000000]
# a = ''
# b = ''
# for i in s:
#     i = float(i)
#     a += struct.pack('<f',i).hex()        #小端
# print(a)
#
# for j in s:
#     i = float(i)
#     b += struct.pack('>f',i).hex()        #小端
# print(b)
#
# a = 0x496e74657265737472696e67204964656120746f20656e6372797074
# b = 0x74707972747079727470797274707972747079727470797274707972
# print(n2s(a))
# print(n2s(b))

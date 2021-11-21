import base64
#十六进制转ASCII
import codecs

m = "024A447B4469664D616E63686573746572636F64657D"
print(codecs.decode(m,'hex'))
#base64
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
# cipher='2559659965656A9A65656996696965A6695669A9695A699569666A5A6A6569666A59695A69AA696569666AA6'
# def iee(cipher):
#     tmp=''
#     for i in range(len(cipher)):
#         a=bin(eval('0x'+cipher[i]))[2:].zfill(4)
#         tmp=tmp+a[1]+a[3] #为什么只取a[1],a[3]???
#         print(tmp)
#     plain=[hex(int(tmp[i:i+8][::-1],2))[2:] for i in range(0,len(tmp),8)] #八个二进制转十六进制
#     print(''.join(plain).upper())
#
# iee(cipher)

#键盘密码
# strr = "ooo yyy ii w uuu ee uuuu yyy uuuu y w uuu i i rr w i i rr rrr uuuu rrr uuuu t ii uuuu i w u rrr ee www ee yyy eee www w tt ee".split()
# all = {'none1':'','none2':'','w':'abc','e':'def','r':'ghi','t':'jkl','y':'mno','u':'pors','i':'tuv','o':'wxyz'}
# for i in strr:
#     print(all[i[0]][len(i)-1],end="")

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


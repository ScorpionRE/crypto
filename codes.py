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


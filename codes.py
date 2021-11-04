

#曼彻斯特
# cipher='5555555595555A65556AA696AA6666666955'
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
strr = "ooo yyy ii w uuu ee uuuu yyy uuuu y w uuu i i rr w i i rr rrr uuuu rrr uuuu t ii uuuu i w u rrr ee www ee yyy eee www w tt ee".split()
all = {'none1':'','none2':'','w':'abc','e':'def','r':'ghi','t':'jkl','y':'mno','u':'pors','i':'tuv','o':'wxyz'}
for i in strr:
    print(all[i[0]][len(i)-1],end="")


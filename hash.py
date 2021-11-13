import hashlib
#a="11 51 51 40 46 51 38"
a = "102 108 97 103 123 119 104 101 110 119 101 116 104 105 110 107 105 116 105 115 112 111 115 115 105 98 108 101 125"
b=a.split(" ")
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

#sha256爆破
flag="PZ5ULgD6vZrXDI48"
m = "729a17a70db54ade76e2650db58a5e4e55f0c6ded39d4e1c5a18acef33b4e8bd"
for x in range(21,127):
    for y in range(21,127):
        for z in range(21,127):
            for q in range(21,127):
                w=hashlib.sha256(str(chr(x) + chr(y) + chr(z) + chr(q) + flag).encode("utf-8"))
                w0=w.hexdigest()

                if(w0==m):
                    print(chr(x)+chr(y)+chr(z)+chr(q)+flag)
                    break
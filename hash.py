import hashlib
a="83 89 78 84 45 86 96 45 115 121 110 116 136 132 132 132 108 128 117 118 134 110 123 111 110 127 108 112 124 122 108 118 128 108 131 114 127 134 108 116 124 124 113 108 76 76 76 76 138 23 90 81 66 71 64 69 114 65 112 64 66 63 69 61 70 114 62 66 61 62 69 67 70 63 61 110 110 112 64 68 62 70 61 112 111 112"
b=a.split(" ")
m="38e4c352809e150186920aac37190cbc"
# flag=""
# for j in range(0,26):
#     flag=""
#     for i in range(len(b)):
#         flag+=chr(int(b[i])-j)
#     print(flag)
flag="flag{www_shiyanbar_com_is_very_good_"

for x in range(21,127):
    for y in range(21,127):
        for z in range(21,127):
            for q in range(21,127):
                w=hashlib.md5(str(flag + chr(x) + chr(y) + chr(z) + chr(q) + "}").encode("utf-8"))
                w0=w.hexdigest()
                print(w0)
                if(w0==m):
                    print(flag+chr(x)+chr(y)+chr(z)+chr(q)+"}")
                    break
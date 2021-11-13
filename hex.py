
#base64
import base64
import codecs

# cipher = b'MyLkTaP3FaA7KOWjTmKkVjWjVzKjdeNvTnAjoH9iZOIvTeHbvD=='
# de_b = base64.b64decode(cipher)
# print(de_b)

#替换base字母表


dict= "JASGBWcQPRXEFLbCDIlmnHUVKTYZdMovwipatNOefghq56rs34ujkxyz012789+/="
base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
cipher='MyLkTaP3FaA7KOWjTmKkVjWjVzKjdeNvTnAjoH9iZOIvTeHbvD=='
res=''
for i in range(len(cipher)):
    for j in range(64):
        if(dict[j]==cipher[i]):
            res+=base64_list[j]
print(res)
missing_padding = 4 - len(res) % 4
if missing_padding:
    res += '=' * missing_padding
flag=base64.b64decode(res)
print(flag)
#b'BJD{D0_Y0u_kNoW_Th1s_b4se_map}'

#hex to ascii
# h = '424a447b57653163306d655f74345f424a444354467d'
# asc = codecs.decode(h,'hex')
# print(asc)
#
# #base32
# cipher_32 = b'J5XGY6JAN5XGKIDTORSXAIDBO5QXSOSRGI4XKWRTJJUGISCWONMVQUTQMIZDK6SPNU4WUYLOII3WK3LUOBRW24BTMJLTQ5DCGJ4HGYLJGF2WEV3YGNGFO4DWMVDWW5DEI4YXMYSHGV4WE3JZGBSG2ML2MZIT2PI='
# de_b32 = base64.b32decode(cipher_32)
# print(de_b32.decode('ascii'))





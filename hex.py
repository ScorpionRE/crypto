
#base64
import base64
import codecs

cipher = b'Q29uZ3JhdHVsYXRpb25zOm9janB7emtpcmp3bW8tb2xsai1ubWx3LWpveGktdG1vbG5ybm90dm1zfQ=='
de_b = base64.b64decode(cipher)
print(de_b)

#hex to ascii
h = '424a447b57653163306d655f74345f424a444354467d'
asc = codecs.decode(h,'hex')
print(asc)

#base32
cipher_32 = b'J5XGY6JAN5XGKIDTORSXAIDBO5QXSOSRGI4XKWRTJJUGISCWONMVQUTQMIZDK6SPNU4WUYLOII3WK3LUOBRW24BTMJLTQ5DCGJ4HGYLJGF2WEV3YGNGFO4DWMVDWW5DEI4YXMYSHGV4WE3JZGBSG2ML2MZIT2PI='
de_b32 = base64.b32decode(cipher_32)
print(de_b32.decode('ascii'))





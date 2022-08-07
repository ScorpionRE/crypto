p = 101762447604961968347497011921099322367324119881977823223715806843654916018223203152717441386396615480134613864942068489600487206751473112264495957512819776729786840027245275219664091321087832913341367749452671938119115622233015167030327196487127307195872792552039408988207189866115101567965404039921455793363
q = 146645055489569596158773422326511843870914610026045288623162173369449741025994927278359852181645222010216728295790096211969513458244344811852179454305768973973420398459241985170762812039623053792853389316411927678494740679905048052776274447299638217155556426312374908963757267001415016478005573936685580868907
N = 14922959775784066499316528935316325825140011208871830627653191549546959775167708525042423039865322548420928571524120743831693550123563493981797950912895893476200447083386549353336086899064921878582074346791320104106139965010480614879592357793053342577850761108944086318475849882440272688246818022209356852924215237481460229377544297224983887026669222885987323082324044645883070916243439521809702674295469253723616677245762242494478587807402688474176102093482019417118703747411862420536240611089529331148684440513934609412884941091651594861530606086982174862461739604705354416587503836130151492937714365614194583664241
e2 = 27188825731727584656624712988703151030126350536157477591935558508817722580343689565924329442151239649607993377452763119541243174650065563589438911911135278704499670302489754540301886312489410648471922645773506837251600244109619850141762795901696503387880058658061490595034281884089265487336373011424883404499124002441860870291233875045675212355287622948427109362925199018383535259913549859747158348931847041907910313465531703810313472674435425886505383646969400166213185676876969805238803587967334447878968225219769481841748776108219650785975942208190380614555719233460250841332020054797811415069533137170950762289
c = 6472367338832635906896423990323542537663849304314171581554107495210830026660211696089062916158894195561723047864604633460433867838687338370676287160274165915800235253640690510046066541445140501917731026596427080558567366267665887665459901724487706983166070740324307268574128474775026837827907818762764766069631267853742422247229582756256253175941899099898884656334598790711379305490419932664114615010382094572854799421891622789614614720442708271653376485660139560819668239118588069312179293488684403404385715780406937817124588773689921642802703005341324008483201528345805611493251791950304129082313093168732415486813
import asymmetric.Rsa as Rsa
# d = Rsa.get_d(65537,p,q)
# Rsa.decrypt(65537,c,d,N)

from binascii import hexlify, unhexlify
from hashlib import md5
from Crypto.Util.number import bytes_to_long,long_to_bytes
from gmpy2 import invert
 
XOR = lambda s1, s2: bytes([x1 ^ x2 for x1, x2 in zip(s1, s2)])
 
 
def inverse_right(res, shift, mask=0xffffffff, bits=32):
    tmp = res
    for i in range(bits // shift):
        tmp = res ^ tmp >> shift & mask
    return tmp
 
 
def inverse_left(res, shift, mask=0xffffffff, bits=32):
    tmp = res
    for i in range(bits // shift):
        tmp = res ^ tmp << shift & mask
    return tmp
 
 
# 逆srand
def recover(last):
    n = 1 << 32
    inv = invert(1812433253, n)
    for i in range(103, -1, -1):
        last = ((last + i) * inv) % n
        last = inverse_right(last, 27)
    return last
 
 
# 逆next
def Last(tmp):
    tmp = inverse_right(tmp, 18, 0x34adf670)
    tmp = inverse_left(tmp, 15, 0xefc65400)
    tmp = inverse_left(tmp, 7, 0x9ddf4680)
    tmp = inverse_right(tmp, 11)
    return tmp
 
 
# 逆state0
cip = b'cef4876036ee8b55aa59bca043725bf3'
assert len(cip) == 32
cip = unhexlify(cip)
tmp = md5('n'.encode()).digest()
key = XOR(tmp, cip)
newstate0 = Last(bytes_to_long(key[:4]))
print(newstate0)
# 逆state103
key = unhexlify(b'b223dde6450ba6198e90e14de107aaf2')
tmp = md5('}'.encode()).digest()
key = XOR(tmp, key)
newstate103 = Last(bytes_to_long(key[-4:]))
print(newstate103)
# 得到oldstate104的两种情况
y_1 = newstate103 ^ newstate0
print(bin(y_1))
if newstate103 >> 31 == 1:
    y = (y_1 ^ 0x9908b0df) << 1 + 1
else:
    y = y_1 << 1
print(bin(y))
oldstate104_1 = (y << 1) >> 1
oldstate104_2 = oldstate104_1 + (1 << 31)
# 验证哪种是对的 这部分有点丑hhh
n = 1 << 32
inv = invert(1812433253, n)
t1 = oldstate104_1
t1 = ((t1 + 103) * inv) % n
t1 = inverse_right(t1, 27)
t2 = oldstate104_1
t2 = ((t2 + 103) * inv) % n
t2 = inverse_right(t2, 27)
oldstate104=0
if t1 & 0x80000000 == y & 0x80000000:
    if t2 & 0x80000000 == y & 0x80000000:
        print('both are right')
    else:
        oldstate104=oldstate104_1
else:
    oldstate104=oldstate104_2
#恢复seed
seed=recover(oldstate104)
print(seed)
 
class mt73991:
    def __init__(self, seed):
        self.state = [seed] + [0] * 232
        self.flag = 0
        self.srand()
        self.generate()
 
    def srand(self):
        for i in range(232):
            self.state[i + 1] = 1812433253 * (self.state[i] ^ (self.state[i] >> 27)) - i
            self.state[i + 1] &= 0xffffffff
 
    def generate(self):
        for i in range(233):
            y = (self.state[i] & 0x80000000) | (self.state[(i + 1) % 233] & 0x7fffffff)
            temp = y >> 1
            temp ^= self.state[(i + 130) % 233]
            if y & 1:
                temp ^= 0x9908f23f
            self.state[i] = temp
 
    def getramdanbits(self):
        if self.flag == 233:
            self.generate()
            self.flag = 0
        #原题的代码下面的这行没int转换
        bits = int(self.Next(self.state[self.flag])).to_bytes(4, 'big')
        self.flag += 1
        return bits
 
    def Next(self, tmp):
        tmp ^= (tmp >> 11)
        tmp ^= (tmp << 7) & 0x9ddf4680
        tmp ^= (tmp << 15) & 0xefc65400
        tmp ^= (tmp >> 18) & 0x34adf670
        return tmp
random = mt73991(seed)
#储存可见字符的md5
S=b''
for i in range(0x20,0x7f):
    S+=long_to_bytes(i)
S_list = []
for i in S:
    tmp = md5(chr(i).encode()).digest()
    S_list.append(tmp)
def decrypt(key, cipher):
    tmp = XOR(key, unhexlify(cipher))
    for i in range(len(S)):
        if S_list[i] == tmp:
            return long_to_bytes(S[i])
    return b''
#开始解密
c = open('./cipher.txt', 'rb').read()
flag = b''
for i in range(len(c)//32):
    key = b''.join([random.getramdanbits() for _ in range(4)])
    cipher = c[i*32:(i+1)*32]
    flag += decrypt(key,cipher)
print(flag)
#reference https://am473ur.com/writeup-for-crypto-problems-in-npuctf-2020/#mersenne_twister
#reference https://0xdktb.top/2020/04/19/WriteUp-NPUCTF-Crypto/

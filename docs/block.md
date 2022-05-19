# AES

## [CISCN2018]sm【逆推】

### 题目

```python
from Crypto.Util.number import getPrime,long_to_bytes,bytes_to_long
from Crypto.Cipher import AES
import hashlib
from random import randint
def gen512num():
    order=[]
    while len(order)!=512:
        tmp=randint(1,512)
        if tmp not in order:
            order.append(tmp)
    ps=[]
    for i in range(512):
        p=getPrime(512-order[i]+10)
        pre=bin(p)[2:][0:(512-order[i])]+"1"
        ps.append(int(pre+"0"*(512-len(pre)),2))
    return ps

def run():
    choose=getPrime(512)
    ps=gen512num()
    print "gen over"
    bchoose=bin(choose)[2:]
    r=0
    bchoose = "0"*(512-len(bchoose))+bchoose
    for i in range(512):
        if bchoose[i]=='1':
            r=r^ps[i]
    flag=open("flag","r").read()

    key=long_to_bytes(int(hashlib.md5(long_to_bytes(choose)).hexdigest(),16))
    aes_obj = AES.new(key, AES.MODE_ECB)
    ef=aes_obj.encrypt(flag).encode("base64")

    open("r", "w").write(str(r))
    open("ef","w").write(ef)
    gg=""
    for p in ps:
        gg+=str(p)+"\n"
    open("ps","w").write(gg)

run()
```



### 解法

#### 一般方法

AES加密flag并base64编码得到密文ef

key为md5(choose)

choose是随机生成的，所以主要需要得到choose

再看bchoose为choose的二进制表示。从前往后遍历，如果为1则异或ps中的对应数。

所以现在已知一个512个数的数表和在其中挑选若干个进行异或的结果，如果要知道都异或了哪些数，计算量为2^512（天文数字中的天文数字），所以一定有其他方法。



所以再分析ps是如何得到的，gen512num()中主要生成生成512个相似结构的512位数字，每个数都由一个长度不定的前缀和‘0’填充组成。**对异或运算来说，只有前缀是有意义的**。而且所有前缀的长度是根据order（1-512的不重复数组）。



我们可以先算出ps中所有数字的前缀的长度，并保存到s中

```python
def pre_num(ps):
    with open(ps,'r') as f:
        ps = f.readlines()
    s = []
    for i in range(len(ps)):
        ps[i] = int(ps[i].strip('\n'))
        num = bin(ps[i])[2:].rfind('1')
        s.append(num)
    print(s)
    return ps,s
```

然后遍历依次还原

```python
def find_choose(r,s,ps):

    with open(r,'r') as f:

        r = int(f.read())
        
    m = list('0'*512)  #bchoose

    for i in range(512):
        if (r>>i) % 2 == 0:
            m[s.index(511-i)] = '0'
        else:
            r = r^ps[s.index(511-i)]
            m[s.index(511-i)] = '1'

    choose = int("0b" + "".join(m), 2)
    print(choose)
    return choose
```

得到choose后解密

```python
key = long_to_bytes(int(hashlib.md5(long_to_bytes(choose)).hexdigest(), 16))
aes_obj = AES.new(key, AES.MODE_ECB)
f2 = open("ef", "rb")
ef = f2.read()
ef = base64.b64decode(ef)
result = aes_obj.decrypt(ef)
```

#### 矩阵

记ps构成的矩阵为 A， 待求的bchoose 为 C， r为B 则:
$$
C*A=B
\\ C=BA^{-1}
$$

```python
#sage代
ps=open('ps','r').readlines()
c=[]
for i in ps:
    c.append(eval(i.strip()))
A=[]
for i in c:
    A.append([int(x) for x in bin(i)[2:].zfill(512)])
r=eval(open('r','r').readline())
B=[int(x) for x in bin(r)[2:].zfill(512)]
A=matrix(GF(2),A)
#print(A.inverse())
B=matrix(GF(2),B)
#print(B)
key=B*A.inverse()
li=[]
for i in key:
   li.append(i)
print(li)
print(key)

```


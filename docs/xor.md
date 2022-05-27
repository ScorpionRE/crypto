# XOR

## ?[AFCTF2018]你听过一次一密么？

一次一密（One-Time-Pad）：xor key  明文多长，密文就多长（适合少量明文消息）

Many-Time-Pad攻击：多个明文异或同样的key

https://www.ruanx.net/many-time-pad/

攻击思想：对于每一条密文Ci，拿去异或其他所有密文。然后去数每一列有多少个英文字符，作为“Mi在这一位是空格”的评分。依据评分从大到小排序，依次利用 “某个明文的某一位是空格” 这种信息恢复出所有明文的那一列。如果产生冲突，则舍弃掉评分小的



**修复语句太绝了**



## ？[De1CTF2019]xorz 【频率分析/break repeating-key】

**法一：流密码**

参考

https://www.anquanke.com/post/id/161171#h3-

http://socold.cn/index.php/archives/65/

### 一.猜测密钥长度

1.暴力破解：

https://www.ruanx.net/many-time-pad/

给的是 m[i]⊕k[i]⊕s[i], 其中 s 已知，故实际上我们拿到了 m[i]⊕k[i]. 在这里 k 是有周期的，且周期不超过38。如果知道了 k 的周期，那么用 Many-Time-Pad 就可以成功攻击。由于 `len(key)` 并不大，从大到小枚举 `len(key)`，肉眼判断是否为flag即可。最后发现 `len(key)=30` 是满足要求的。

但是这种方法过于耗时费力

2.汉明距离：一组二进制数据变成另一组数据所需的步骤数。对两组二进制数据进行异或运算，并统计结果为1的个数，那么这个数就是汉明距离。

- 根据扩展资料：

  - 两个以ascii编码的英文字符的汉明距离是2-3之间，也就是说正常英文字母的平均汉明距离为2-3（每比特），任意字符（非纯字母）的两两汉明距离平均为4。

  - 正确分组的密文与密文的汉明距离等于明文与明文的汉明距离（可以通过按正确密钥长度分组的密文与密文异或等于明文与明文异或证明）

    因此，当我们使用了正确的密钥长度后，两两字母进行计算汉明距离，那么这个值应该是趋于最小。为了增加效率，我们不需要对每一对分组都计算汉明距离，只需取出前几对就可说明问题。当然为了排除偶然误差，结果不应该只取最小的那一个密钥长度，而是酌情多取几组



### 二.根据猜出的密文长度进行解密

两种方法：

- 合理利用明文的空格

  在使用异或加密的形式下，使用相同密钥加密的明文和秘文间存在这个规律，密文和密文异或等于明文和明文异或,并且二者的汉明距离一样。

  空格和所有小写字母异或结果是相应的大写字母，空格和所有大写字母异或是相应的小写字母。

  ![img](xor.assets/t01dd9c90c1ecde8471.jpg)

  ![img](xor.assets/t0189dac1c8ab2412c8.jpg)

 	1. 使用取模运算把密文分成n个分组（其中n是密钥长度），如此以来，我们就有了n个独立的凯撒加密式的密文组（因为每个分组里面的值是使用同一个密钥字节明文异或）。这样就把问题简化成了破解n个独立的凯撒加密模式的单字节抑或密码方式。这一步可以直接使用爆破，但是效率不高。我们采取另一种姿势。 
 	2. 将2中的每个分组做如下的操作：每个分组做嵌套循环，内循环，外循环。设置外循环计数值possible*_space=0，max_*possible=0，设置内循环计数值maxpossible=0,依次取出每个分组中的每一个字节做与其他字节两两抑或进行内循环，如果结果是字母，我们就把内循环计数值maxpossible+1,在每个内循环结束后进行max*_possible的更新（与内循环maxpossible做对比），并记录当前字节的位置到possible_*space，然后外循环继续。直至遍历完所有的字节。取出max*_possible对应的字节位置possible_*space处的字节码，我们把它对应的明文假设成空格（根据之前的讨论）然后将该位置的字节和0x20（空格）异或;找出相应位置的密钥字节。 

3. 重复2中的步骤，依次根据每个分组找出每位的密钥字节，至此密钥破解完毕 

4. 将找出的密钥用于破解密文。当密文足够多，可以发现破解的准确率很高，基本可以做到无差别破解。



**词频分析**

https://codeleading.com/article/68135872581/



## [BSidesSF2020]decrypto-1【循环】

### 题目

说明.txt : 

[Kerckhoffs's principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle) states that "A cryptosystem should be secure even if everything about the system, except the key, is public knowledge."  So here's our unbreakable cipher.



flag.txt.enc

decrypto.py

```python
import sys
import json
import hashlib


class Crypto:

    def __init__(self, key):
        if not isinstance(key, bytes):
            raise TypeError('key must be of type bytes!')
        self.key = key
        self._buf = bytes()
        self._out = open("/dev/stdout", "wb")

    def _extend_buf(self):
        self._buf += self.key

    def get_bytes(self, nbytes):
        while len(self._buf) < nbytes:
            self._extend_buf()
        ret, self._buf = self._buf[:nbytes], self._buf[nbytes:]
        return ret

    def encrypt(self, buf):
        if not isinstance(buf, bytes):
            raise TypeError('buf must be of type bytes!')
        stream = self.get_bytes(len(buf))
        return bytes(a ^ b for a, b in zip(buf, stream))

    def set_outfile(self, fname):
        self._out = open(fname, "wb")

    def encrypt_file(self, fname):
        buf = open(fname, "rb").read()
        self._out.write(self.encrypt(buf))


class JSONCrypto(Crypto):

    def encrypt_file(self, fname):
        buf = open(fname, "r").read().strip()
        h = hashlib.sha256(buf.encode('utf-8')).hexdigest()
        data = {
                "filename": fname,
                "hash": h,
                "plaintext": buf,
        }
        outbuf = json.dumps(data, sort_keys=True, indent=4)
        self._out.write(self.encrypt(outbuf.encode("utf-8")))


def main(argv):
    if len(argv) not in (3, 4):
        print("%s <key> <infile> [outfile]" % sys.argv[0])
        return
    argv.pop(0)
    key = argv.pop(0)
    inf = argv.pop(0)
    crypter = JSONCrypto(key.encode("utf-8"))
    if sys.argv:
        crypter.set_outfile(argv.pop(0))
    crypter.encrypt_file(inf)


if __name__ == '__main__':
    main(sys.argv)

```



### 解法

先看加密过程：实际上是data和key之间的异或操作，所以主要还是需要得到key。

一般来说，key不会太长、根据加密文档flag.txt.enc，推测被加密的filename为flag.txt，这样data的长度超过了15，所以可以构造data并与密文异或，观察key，可以发现出现了循环，那么这就很可能是key。

最后用key和data异或，得到明文内容

```python
import json
fp=open("flag.txt.enc","rb")
b=fp.read()
fp.close()
data = {
            "filename": 'flag.txt',
            "hash": ' ',
            "plaintext":' '
        }
outbuf = json.dumps(data, sort_keys=True, indent=4)
s=""
for i in range(min(len(outbuf),len(b))):
    s+=chr(b[i]^ord(outbuf[i]))
print(s)

key=b'n0t4=l4g'
ans=''
for i in range(len(b)):
    ans+=chr(b[i]^key[i%len(key)])
print(ans)
```


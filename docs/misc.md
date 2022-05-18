## [Zer0pts2020]ROR

### 题目

```python
import random
from secret import flag

ror = lambda x, l, b: (x >> l) | ((x & ((1<<l)-1)) << (b-l))  #循环右移

N = 1
for base in [2, 3, 7]:
    N *= pow(base, random.randint(123, 456))  # 2^n*3^n*7^n
e = random.randint(271828, 314159)

m = int.from_bytes(flag, byteorder='big')
assert m.bit_length() < N.bit_length()

for i in range(m.bit_length()):
    print(pow(ror(m, i, m.bit_length()), e, N))




```

### 解法

N是个2的倍数，而一个数如果对一个偶数取模，那么其奇偶性不变。而乘方运算是不改变一个数字的奇偶性的。所以这道题给出的数字中，每个数字都泄露了明文的最后一个比特位，拼接起来就是flag

```python
with open("chall.txt",'r') as f:
    m = f.readlines()

flag = ""
for i in range(len(m)):
    m[i] = m[i].strip("\n")
    flag += bin(int(m[i]))[-1]

print(long_to_bytes(int(flag,2)))
print(long_to_bytes(int(flag[::-1],2)))
```


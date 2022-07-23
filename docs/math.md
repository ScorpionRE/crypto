# 基础知识

## 连分数

数x表示为如下形式

![image-20211220201601164](math.assets/image-20211220201601164.png)

可以
$$
x=[a 
0
​
 ,a 
1
​
 ,a 
2
​
 ,a 
3
​
 ,…,a 
n
​
 ]
$$
例子：

![image-20211220202843285](math.assets/image-20211220202843285.png)

```python
        def continuedfra(x,y):
            cf = []
            while y:
                cf += [x//y]
                x,y = y,x%y
            return cf

        n = continuedfra(73,95)
        print(n)
```



## 离散对数

n1=p1q1，则ord(p1)=q1，因为
$$
p1^x mod n 
$$
的值只有q1种结果

## 数论

### 同余

![img](math.assets/webp.webp)

### 欧拉定理

![a^{{\varphi (n)}}\equiv 1{\pmod  n}](math.assets/2e818f3f88d3e71e569f171dd86f31e1903fdc55.svg+xml)
$$
m^{p-1} = 1 mod p (p为素数)
$$

### 欧拉函数

![image-20211204192438892](math.assets/image-20211204192438892-16419928116143.png)

### 欧拉准则

给定非零n，**奇素数p**

n有一个平方根（二次余数）当且仅当
$$
n^{p-1/2} = 1 (mod\ p)
$$
若n没有平方根
$$
n^{p-1/2} = -1 (mod\ p)
$$

可以通过此判断n是否为p的二次剩余

### 欧几里得算法



### 扩展欧几里得



### 中国剩余定理





### 指数循环节





## 抽象代数



# 题目

## [CISCN]puzzle【】

### 题目

![image-20220524213218362](math.assets/image-20220524213218362.png)

![image-20220524213227849](math.assets/image-20220524213227849.png)

### 解法

是真的不能再绝了（ ~~`sos`~~

#### question 0 【方程组】

解方程即可

```python
x = sympy.Symbol('x')
y = sympy.Symbol("y")
z = sympy.Symbol("z")
m = sympy.Symbol("m")

solved_value = sympy.solve([13627*x + 26183*y + 35897*z + 48119*m -347561292 ,
                            23027*x + 38459*y + 40351*z + 19961*m -361760202,
                            36013*x + 45589*y + 17029*z + 27823*m -397301762,
                            43189*x + 12269*y + 21587*z + 33721*m -350830412], [x,y,z,m])
print(solved_value)

```

得到{x: 4006, y: 3053, z: 2503, m: 2560}

fa6bed9c7a00

#### question 1【找规律】

刚开始还以为会有等差数列什么的（

但是发现不对，再发现好像都是素数（ctf 密码也经常接触素数，应该就是相邻的素数

26365399 (0x1924dd7)

#### question 2【极限、积分】

```python
# 极限
x = sympy.Symbol('x')
f = (x**2 -3*x + 2)/(x**2-4)
print(sympy.limit(f,x,2))

# 积分
f = sympy.exp(x)*(4+sympy.exp(x))**2
print(sympy.integrate(f,(x,0,sympy.ln(2))))

f2 = (1 + 5*sympy.ln(x))/x
print(sympy.integrate(f2,(x,1,sympy.exp(1))))

f3 = x*sympy.sin(x)
print(sympy.integrate(f3,(x,0,sympy.pi/2)))
```



#### question 3【电磁感应】

![img](math.assets/3FBFDED7D8490179D1D0C09388321A6E.png)

18640 (0x48d0)

#### question 4【fubini定理】



https://www.zybang.com/question/aed760f3251be1a87a2ab0d2069eb295.htmlhttps://www.zybang.com/question/aed760f3251be1a87a2ab0d2069eb295.html

![image-20220524221735121](math.assets/image-20220524221735121.png)40320 (0x9d80)



## [GKCTF2021]XOR【dfs，x+n+len->a,b】

### 题目

已知奇数相乘与异或的结果

```python
a = getPrime(512)
b = getPrime(512)
c = getPrime(512)
d = getPrime(512)
d1 = int(bin(d)[2:][::-1] , 2)
n1 = a*b
x1 = a^b
n2 = c*d
x2 = c^d1
flag = md5(str(a+b+c+d).encode()).hexdigest()
```



### 解法

已知a，b都为512位的奇数，现已知其积n1，异或结果x1，需要求a，b的值

所以只需要不断枚举它的每一位就可以了。但是每位有0，1两种结果，512位就有2^512种可能，显然爆破是不太现实的。

不过有这样一个同余的性质：不论在几进制下，如果已知A,B两个数的最后n位，那么它们的乘积的最后n位我们也会知道了。

例如：

**9**×**7**=6**3**，53370**9**×18826**7**=10047979230**3**。

十六进制这种情况也同样存在：

7ABH×96FH=485625H，8733**7AB**H×62CEH**96F**H=342ED01B03C**625**H



所以我们需要逐位根据条件得到可能的（a,b）对，每次更新a和b的表，主要根据以下两个条件：

1. 新的aa和bb符合异或结果，即
   $$
   aa\ xor \ bb == x1 \ mod \ 2^{round}
   $$
   

2. 乘积与n1的后round位相同，即
   $$
   aa * bb \ mod \  2^{round} == n1 \ mod \ 2^{round}
   $$

重复上述步骤，只需要n（512）次即可找到

然后依次判断a,b是否满足条件，即乘积是否为n1

```python
# DFS，已知a，b的积n，异或结果x，求a，b。 len为a，b的比特位
def dfs(n,x,len):
    a_list, b_list = [0], [0]

    round = 1
    for i in range(len):  # 已知a和b的低n(512)位的异或结果
        round *= 2
        nxt_as, nxt_bs = [], []
        for al, bl in zip(a_list, b_list):
            for ah, bh in itertools.product([0, 1], repeat=2):
                aa, bb = ah * (round // 2) + al, bh * (round // 2) + bl
                if ((aa * bb % round == n % round) and ((aa ^ bb) == x % round)):
                    nxt_as.append(aa)
                    nxt_bs.append(bb)

        a_list, b_list = nxt_as, nxt_bs

    for a, b in zip(a_list, b_list):
        if (a * b == n):
            break

    print(a)
    print(b)
    return a,b

```

递归版本 https://huangx607087.online/2021/07/12/GKCTF2021-WriteUp/#toc-heading-8



求c，d同理，但是题目已知的是d的二进制倒序d1 与 c异或的结果x2

因此爆破时，同时爆破4个位，即c、d的高位c_high_bit、d_high_bit，c、d的低位c_low_bit、d_low_bit 。此时验证条件改为：

（1）c_low_bit ^ d_high_bit == x2_low_bit

（2）c_high_bit ^ d_low_bit == x2_high_bit

（3）(c_low_bit[:-i] * d_low_bit[:-i]) mod (2^i )== n2_low_bit mod (2^i )

（4）(c_high_bits + c_low_bits) * (d_high_bits + d_low_bits ) <= n2

（5）(c_high_bits + c_low_bits + 中间位全1) * (d_high_bits + d_low_bits + 中间位全1) >= n2

```python
def dfs2(x,n,len):
    a_list, b_list, aa_list, bb_list = [0], [0], [0], [0]

    x1_bits = [int(x) for x in f'{x:0512b}'[::-1]]

    cur_mod = 1
    for i in range(len//2):  # 分别从高位和低位 逐位更新，所以只需要n/2次
        cur_mod *= 2
        nxt_as, nxt_bs, nxt_aas, nxt_bbs = [], [], [], []
        for al, bl, a2, b2 in zip(a_list, b_list, aa_list, bb_list):
            for ah, bh, ah2, bh2 in itertools.product([0, 1], repeat=4):
                aa, bb, aa2, bb2 = ah * (cur_mod // 2) + al, bh * (cur_mod // 2) + bl, ah2 * (cur_mod // 2) + a2, bh2 * (
                            cur_mod // 2) + b2
                bb2_rev = f'{bb2:0512b}'[::-1]
                bb2_rev = int(bb2_rev, 2)
                aa2_rev = f'{aa2:0512b}'[::-1]
                aa2_rev = int(aa2_rev, 2)

                gujie = '0' * (i + 1) + '1' * (510 - 2 * i) + '0' * (i + 1)
                gujie = int(gujie, 2)
                if ((aa * bb % cur_mod == n % cur_mod) and ((ah ^ bh2) == x1_bits[i]) and (
                        ah2 ^ bh == x1_bits[511 - i]) and ((aa2_rev + aa) * (bb2_rev + bb) <= n) and (
                        (aa2_rev + aa + gujie) * (bb2_rev + bb + gujie) >= n)):
                    nxt_as.append(aa)
                    nxt_bs.append(bb)
                    nxt_aas.append(aa2)
                    nxt_bbs.append(bb2)

        a_list, b_list, aa_list, bb_list = nxt_as, nxt_bs, nxt_aas, nxt_bbs

    for a, b, aa2, bb2 in zip(a_list, b_list, aa_list, bb_list):
        aa2_rev = f'{aa2:0512b}'[::-1]
        aa2_rev = int(aa2_rev, 2)
        bb2_rev = f'{bb2:0512b}'[::-1]
        bb2_rev = int(bb2_rev, 2)
        a = aa2_rev + a
        b = bb2_rev + b
        if (a * b == n):
            break

    print(a)
    print(b)
    print(a*b==n)
    return a,b
```


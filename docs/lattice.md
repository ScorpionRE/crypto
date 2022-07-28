# 基础

**格的定义**：设$v_1,\dots,v_n\in{R^n}$ 为一组线性无关的向量，即**基向量**。**格$L$**指的是向量$v_1,\dots,v_n$的线性组合构成的向量集合，且其所使用的系数均在$Z^n$中，即
$$
L={a_1
​
 v_1
​
 +a_2
​
 v_2
​
 +⋯+a_n
​
 v_n
​
 :a_1
​
 ,a_2
​
 ,…,a_n
​
 ∈Z}
$$
**格的基**：任意一组可以生成格的线性无关的向量，格的基中的向量个数称为格的**维度**。任意两组基向量中，向量的个数相同

（二维坐标系可以看做一个格。每个格有很多组格基，格基的线性组合可以得到格中全部的点（==但是格中基向量系数为整数，二维平面中基向量系数为实数==）。对于二维坐标系，向量 (1,0) 和 (0,1) 就是最简单的一组格基）

**最短向量问题 (Shortest Vector Problem, SVP).** SVP 问题定义为：对于给定的格 $L$ ，找到一个非零的格向量 $v$ ，使得对于任意的非零向量 $u \in L, ||v|| \leq ||u||$

**最近向量问题 (Closest Vector Problem, CVP).** CVP 问题定义为：对于给定的格 $L$ 和不在格中的目标向量 $t∈R^m$，找到一个非零的格向量 $v$，使得对于任意的非零向量 $u∈L,||v-t|| \leq ||u-t||$

**容错学习问题 (Learning with Errors Problem, LWE).** LWE 问题定义为：给定均匀随机生成的矩阵 $A∈Z_q^{m×n}$， $s∈Z_q^n$和 $e∈Z_q^m$ 服从分布 $χ$， $b_i=A_is+e_i$。搜索版本的 LWE 问题（Search LWE）为：给定多组 $(Ai,bi)$，找到 $s$。判定版本的 LWE 问题（Decision LWE）为：将 $bi$ 和均匀随机生成的向量区分开
**环上容错学习问题 (Ring Learning with Errors Problem, RLWE).** RLWE 问题定义为：给定均匀随机生成的多项式 $a∈R^q$， $s∈R^q$ 和 $e∈R^q$ 服从分布 $χ$， $b_i=a_is+e_i$。搜索版本的 RLWE 问题 (Search RLWE) 为：给定多组 $(ai,bi)$，找到 $s$。判定版本的 RLWE 问题 (Decision RLWE) 为：将 $bi$和均匀随机生成的向量区分开

# 题目

## [watevf2019]babyRLWE【RLWE】

### 题目

一个sage文件以及公钥文件

```python
from sage.stats.distributions.discrete_gaussian_polynomial import DiscreteGaussianDistributionPolynomialSampler as d_gauss

flag = bytearray(raw_input())
flag = list(flag)

n = len(flag)
q = 40961

## Finite Field of size q. 
F = GF(q)

## Univariate Polynomial Ring in y over Finite Field of size q
R.<y> = PolynomialRing(F)

## o Quotient Polynomial Ring in x over Finite Field of size 40961 with modulus b^n + 1
S.<x> = R.quotient(y^n + 1)

def gen_small_poly():
    sigma = 2/sqrt(2*pi)
    d = d_gauss(S, n, sigma)
    return d()

def gen_large_poly():
    return S.random_element()


## Public key 1
a = gen_large_poly()

## Secret key
s = S(flag)


file_out = open("downloads/public_keys.txt", "w")
file_out.write("a: " + str(a) + "\n")


for i in range(100):
    ## Error
    e = gen_small_poly()

    ## Public key 2
    b = a*s + e
    file_out.write("b: " + str(b) + "\n")

file_out.close()

```



### 解法

根据题目，很明显为搜索版本的RLWE问题，其中b1(x)到b100(x)已知，a(x)已知，e1(x)到e100(x)未知，求s(x)

```
b1(x) = a(x)*s(x) + e1(x)
b2(x) = a(x)*s(x) + e2(x)
...
b100(x) = a(x)*s(x) + e100(x)

```

先看代码其中a（x）是通过gen_large_poly()生成的，e（x）是通过gen_small_poly()生成的，而此时还不知道其中一些特征

观察给出的文件，其中a(x)的多项式中系数均不为0，最高次数为103，那么我们推测n为103+1=104。

同时，sage中测试一下gen_small_poly()生成的e(x)，发现有些项不存在，即有的项系数为0。

所以a(x)*s(x)后再加上e(x)，很多项b(x)就是等于a(x) * s(x)，而题目给出了许多b(x)的值，所以可以直接统计b(x)中x^n项系数出现频率最高的，直接作为a(x)* b(x)的对应项的系数，这样可以求得s(x)中对应项的系数，依次类推，直到求得s(x)。

另外，要注意a(x)和s(x)都是限制在$S.<X>=R.quotient(y^n+1)$范围中，因此也要先对每个b(x)进行b(x) = S(b(x))的处理，然后进行运算。

```python

#sage
from sage.stats.distributions.discrete_gaussian_polynomial import DiscreteGaussianDistributionPolynomialSampler as d_gauss
keys = open("public_keys.txt", "r").read().split("\n")[:-1]
temp1 = keys[0].find("^")
temp2 = keys[0].find(" ", temp1)
n=int(keys[0][temp1+1:temp2])+1
print(n)
q = 40961
F = GF(q)
R.<y> = PolynomialRing(F)
S.<x> = R.quotient(y^n + 1)
num=[]
for i in range(n):
    num.append({})
#print(num)
a=S(keys[0].replace('a: ',''))
#print(a)
keys=keys[1:]
for key in keys:
    b=key.replace('b: ','')
    li=list(S(b))
    #print(li)
    for i in range(len(num)):
        try:
            num[i][li[i]]+=1
        except:
            num[i][li[i]]=1
asnum=[]
#print(num)
for i in num:
    asnum.append(max(i,key=i.get))  #{key:value}分别表示系数，系数出现次数。
#print(asnum)
aspoly=S(asnum)
flag=aspoly/a
print(list(flag))
flag=''.join(map(chr,flag))
print(flag)


```


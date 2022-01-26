# [ichunqiu-crypto]writeup

### [phrackCTF]BrokenPic

题面：这里有个图片，可是好像打不开？



给出一个bmp图片





## RSA

### [IceCTF]Round Rabins【Cipolla算法】

发现n能开平方，提示rabin，e应为2，所以转化为下式求m的值
$$
c = m^2 (mod\ p^2)
$$
先利用Cipolla算法求得r，使得
$$
a = r^2 (mod\ p)
\\所以 (r^2-a)^k = 0 (mod\ p^k)
\\二项式分解 (r^2-a)^k=t^2-u^2a=0(mod\ p^k)
\\t^2u^{-2} = a = x^2(mod\ p^k)
\\所以 x = t*u^{-1} (mod p^k)
$$
利用平方差公式得到方程组，求解得t、u
$$
（r-\sqrt[2]{a})^k = t-u\sqrt[2]{a}
\\(r+\sqrt[2]{a})^k = t + u\sqrt[2]{a}
$$
**Cipolla算法**



更一般的情况：先对n进行质因数分解，再使用中国剩余定理
$$
n=p1^{k1} * p2^{k2} * p3^{k3}
$$

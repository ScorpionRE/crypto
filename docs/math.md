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


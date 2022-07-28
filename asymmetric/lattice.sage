
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



import copy
import pyDes
key='********'
d=pyDes.des(key)
key10=[0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
PC1=[56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 60, 52, 44, 36, 28, 20, 12, 4, 27, 19, 11, 3]
PC2=[13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9, 22, 18, 11, 3, 25, 7, 15, 6, 26, 19, 12, 1, 40, 51, 30, 36, 46, 54, 29, 39, 50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]
movnum = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1] #对应16轮中每一轮的循环左移位数
def gen_key(C1,D1,k):
    tempc=C1
    tempd=D1
    for i in range(k):
        tempc = tempc[1:] + tempc[:1]
        tempd = tempd[1:] + tempd[:1]
    tempCD1=tempc+tempd
    tempkey=[]
    for i in range(len(PC2)):
        tempkey.append(tempCD1[PC2[i]])
    return (tempkey,tempCD1)#轮运算得到下一轮子密钥
def re_gen_key(C1,D1):
    tempc=C1[-1:]+C1[:-1]
    tempd=D1[-1:]+D1[:-1]
    tempCD1=tempc+tempd
    return tempCD1 #轮运算得到上一轮CD
def get_key(CD):
    tempkey=[]
    for i in range(len(PC2)):
        tempkey.append(CD[PC2[i]])
    return tempkey
def RE_pc2():
    CD1=['*']*56
    for i in range(len(PC2)):
        CD1[PC2[i]]=key10[i] #初步还原CD1
    results=[]
    for i in range(256):
        temp=bin(i)[2:].zfill(8)
        tempi=copy.deepcopy(CD1)
        d=0
        for j in range(len(tempi)):
            if tempi[j]=='*':
                tempi[j]=eval(temp[d])
                d=d+1
        results.append(tempi)
    return results
f=open('cipher','rb')
flag_enc=f.read()
results=RE_pc2()
for i in range(len(results)):
    temp=results[i]
    for j in range(sum(movnum[:11])):
        temp=re_gen_key(temp[:28],temp[28:])
    tempK=[]
    Z=temp
    for j in range(16):
        tempx=gen_key(Z[:28],Z[28:],movnum[j])
        tempK.append(tempx[0])
        Z=tempx[1]
    d.Kn=tempK
    print(d.decrypt(flag_enc))


#b'NCTF{1t_7urn3d_0u7_7h47_u_2_g00d_@_r3v3rs3_1snt}'


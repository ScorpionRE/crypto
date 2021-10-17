import primefac


def zhalan_encrypt(m,k):
    chip = []
    for i in range(0,len(m),k):
        if i + k >= len(m):
            tmp_m = m[i:]
        else:
            tmp_m = m[i:i+k]
        chip.append(tmp_m)
    c = ""
    for i in range(k):
        for tmp_m in chip:
            if i < len(tmp_m):
                c += tmp_m[i]
    return c

'''
def zhalan_decrypt(c,k):
    l=len(c)
    partnum=l/k
    if l%k!=0:
        partnum+=1
    m=[""]*l
	
    for i in np.arange(0.0,1.0,partnum):
        if i+partnum>=len(c):
            tmp_c=c[i:]
        else:
            tmp_c=c[i:i+partnum]
        for j in range(len(tmp_c)):
            m[j*k+i/partnum]=tmp_c[j]

    return "".join(m)
'''
def caesar_128_encrypt(m,k):
    r=""
    for i in m:
        r+=chr((ord(i)+k)%128)
    return r
def caesar_128_decrypt(c,k):
    r=""
    for i in c:
        r+=chr((ord(i)-k)%128)
    return r
def caesar_128_brute(c,match_str):
    result=[]
    for k in range(128):
        tmp=caesar_128_decrypt(c,k)
        if match_str in tmp:
            result.append(tmp)
    return result
def caesar_128_bruteall(c):
    result=[]
    for k in range(128):
        tmp=caesar_128_decrypt(c,k)
        result.append(tmp)
    return result

#仿射密码

def affine_encode(m,a,b,origin="abcdefghijklmnopqrstuvwxyz"):
    r=""
    for i in m:
        if origin.find(i)!=-1:
            r+=origin[(a*origin.index(i)+b)%len(origin)]
        else:
            r+=i
    return r
def affine_decode(c,a,b,origin="abcdefghijklmnopqrstuvwxyz"):
    r=""
    n=len(origin)
    ai=primefac.modinv(a,n)%n
    for i in c:
        if origin.find(i)!=-1:
            r+=origin[(ai*(origin.index(i)-b))%len(origin)]
        else:
            r+=i
    return r
def affine_brute(c,origin="abcdefghijklmnopqrstuvwxyz"):
    result=[]
    for a in range(len(origin)):
        for b in range(len(origin)):
            result.append(affine_decode(c,a,b,origin))
    return result
def affine_guessab(m1,c1,m2,c2,origin="abcdefghijklmnopqrstuvwxyz"):
    x1=origin.index(m1)
    x2=origin.index(m2)
    y1=origin.index(c1)
    y2=origin.index(c2)
    n=len(origin)
    dxi=primefac.modinv(x1-x2,n)%n
    a=dxi*(y1-y2) % n
    b=(y1-a*x1)%n
    return (a,b)



if __name__ == '__main__':
    m  = "flag{zhalan_mima_hahaa}"
    k = 4
    c = zhalan_encrypt(m,k)
    print(c)
    affine_encode()
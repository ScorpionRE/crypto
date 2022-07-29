out=[8886, 42, 212351850074573251730471044, 424970871445403036476084342 ,5074088654060645719700112791577634658478525829848, 17980375751459479892183878405763572663247662296, 121243943296116422476619559571200060016769222670118557978266602062366168 ,242789433733772377162253757058605232140494788666115363337105327522154016 ,2897090450760618154631253497246288923325478215090551806927512438699802516318766105962219562904, 7372806106688864629183362019405317958359908549913588813279832042020854419620109770781392560]
#out.append((out[i+1] + ((out[i] * ord(plaintext[i])) ^ (key+out[i+1]))) ^ (key*out[i]))
# plaintext[i] = chr() 
plain='Houdini:'
from z3 import*
for count in range(2,78):
    key=BitVec('key',count)
    s=Solver()
    for i in range(8):
        s.add(((out[i + 1] + ((out[i] * ord(plain[i])) ^ (key + out[i + 1]))) ^ (key * out[i]))==out[i+2])
    s.check()
    res=s.model()
    print(res)
    res = res[key].as_long().real
    print(res)
    f=open('conversation','r').readlines()
    x=[]
    for j in f:
        x.append(j.strip())
    flag=''
    for j in range(1,len(x),2):
        li=x[j].split(' ')
        for k in range(1,len(li)):
            li[k]=eval(li[k])
        for k in range(1,len(li)-2):
            try:
                flag += chr(((res + li[k + 1]) ^ (((res * li[k]) ^ li[k + 2]) - li[k + 1])) // li[k])
            except:
                break
    if 'watevr{' in flag:
        print(flag)
        break

from threading import Thread
import base36

p=11360738295177002998495384057893129964980131806509572927886675899422214174408333932150813939357279703161556767193621832795605708456628733877084015367497711
c1=int('a9hgrei38ez78hl2kkd6nvookaodyidgti7d9mbvctx3jjniezhlxs1b1xz9m0dzcexwiyhi4nhvazhhj8dwb91e7lbbxa4ieco',36)
def calr(r0,pid):
    print("[Process%d]: start from %d" % (pid, r0))
    while r0 < 2**26*(pid+1):
        if pow(2,r0,p) == c1:
            f = open('r','w')
            f.write(r0)
            global r
            r = r0
            exit(0)
        r0+=1
        if r0 % 2**18 == 0:
            print('[Process%d]: now %d' % (pid, r0))
    print('[Process%d]: exited!' % pid)

for i in range(0,32):
    t = Thread(target=calr,args=(i*2**26,i))
    t.start()
#152351913

c2 = int('2q17m8ajs7509yl9iy39g4znf08bw3b33vibipaa1xt5b8lcmgmk6i5w4830yd3fdqfbqaf82386z5odwssyo3t93y91xqd5jb0zbgvkb00fcmo53sa8eblgw6vahl80ykxeylpr4bpv32p7flvhdtwl4cxqzc', 36)
h = int("7854998893567208831270627233155763658947405610938106998083991389307363085837028364154809577816577515021560985491707606165788274218742692875308216243966916")
print(base36.dumps(c2//pow(h,r,p)))
#ciscncongratulationsthisisdesignedbyalibabasecurity424218533


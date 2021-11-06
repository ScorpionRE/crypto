import codecs

import gmpy2

a = [0x61707478, 0x34383639]
#a = [0x34383639,0x61707478]
cmpp = [[0x0712BD3E, 0x2926B771], [0x31CE29D1, 0x30D01980], [0x0F892190, 0X1F99C58B], [0x247346F8, 0x22F3FA31]]


def CRT(k, a, r):
    n = 1;
    ans = 0
    for i in range(0, k + 1):
        n = n * r[i]
    for i in range(0, k + 1):
        m = gmpy2.mpz(n / r[i]);
        b = y = 0
    # exgcd(m, r[i], b, y) # b * m mod r[i] = 1
        b = gmpy2.invert(m, r[i])
        ans = (ans + a[i] * m * b % n) % n
    return (ans % n + n) % n


output = [0 for i in range(4)]
#s = ""
s = []
for i in range(4):
    output[i] = CRT(1, cmpp[i], a)
    #print(hex(output[i]))
    print(hex(output[i])[-1:-8])
    #print(codecs.decode(hex(output[i])[2:],'hex'))
    temp = output[i]
    for j in range(8):
        #s += chr(int(str(temp & 0xFF),16))
        s.append(int(str(temp & 0xFF),16))
        #print(temp & 0xff)
        temp //= 0x100
print(output)
print(s)

from Crypto.Util.number import * 
from gmpy2 import invert, sqrt, gcd 
from string import ascii_letters, digits 
from hashlib import sha256 
from pwn import * 
from pwnlib.util.iters import mbruteforce 
context.log_level = 'debug' 
def proof_of_work(p): 
    p.recvuntil("XXX+") 
    suffix = p.recv(17).decode("utf8") 
    p.recvuntil("== ") 
    cipher = p.recvline().strip().decode("utf8") 
    proof = mbruteforce(lambda x: sha256((x + suffix).encode()).hexdigest() == 
                        cipher, string.ascii_letters + string.digits, length=3, method='fixed') 
    p.sendlineafter("Give me XXX:", proof) 
def rational_to_contfrac(x,y): 
    a = x // y 
    pquotients = [a] 
    while a * y != x: 
        x,y = y, x - a * y 
        a = x // y 
        pquotients.append(a) 
    return pquotients 
def convergents_from_contfrac(frac): 
    convs = [] 
    for i in range(len(frac)): 
        convs.append(contfrac_to_rational(frac[0:i])) 
    return convs 
def contfrac_to_rational (frac): 
    if len(frac) == 0: 
        return (0, 1) 
    num = frac[-1] 
    denom = 1 
    for _ in range(-2, -len(frac) - 1, -1): 
        num, denom = frac[_] * num + denom, num 
    return (num, denom) 
def get_d(q, h, c, N, ct): 
    frac = rational_to_contfrac(h, q) 
    convergents = convergents_from_contfrac(frac) 
    for (i, f) in convergents: 
        g = abs(h * f - i * q) 
        try: 
            cake = (c * f % q * invert(f, g) % g) 
            if pow(cake, f, N) == ct: 
                return f 
        except: 
            continue 
def make_cake(): 
    Ns = [] 
    ds = [] 
    num = 14 
    for i in range(num): 
        print("Getting the {} / {} d".format(str(i + 1), str(num))) 
        io = remote('node4.buuoj.cn', 28602)
        proof_of_work(io) 
        io.sendafter('What\'s your choice?\n', '2\n') 
        io.recvline() 
        q, h, c = [int(x) for x in io.recvline(keepends = False).decode().split(' ')] 
        N = int(io.recvline(keepends = False)) 
        Ns.append(N) 
        ds.append(get_d(q, h, c, N, int(io.recvline(keepends = False)))) 
        io.close() 
    M = 1 
    for i in range(num): 
        if int(sqrt(Ns[i])) > M: 
            M = int(sqrt(Ns[i])) 
    B = matrix(ZZ, num + 1, num + 1) 
    B[0, 0] = M 
    for i in range(1, num + 1): 
        B[0, i] = ds[i - 1] 
    for i in range(1, num + 1): 
        B[i, i] = -Ns[i - 1] 
    return abs(B.LLL()[0, 0] // M) 
def get_ans(q,h,e, N, ct): 
    frac = rational_to_contfrac(h, q) 
    convergents = convergents_from_contfrac(frac) 
    for (i, d) in convergents: 
        p = gcd(int(pow(2, e * d - 1,N) - 1), N) 
        if p > 1 and p < N: 
            return pow(ct, invert(0x10001, (p - 1) * (N//p - 1)), N) 
def eat_cake(e): 
    io = remote('node4.buuoj.cn', 28602)
    proof_of_work(io) 
    io.sendafter('What\'s your choice?\n', '1\n') 
    io.recvline() 
    q, h, c = [int(x) for x in io.recvline(keepends = False).decode().split(' ')]
    N = int(io.recvline(keepends = False))
    ct = int(io.recvline(keepends = False))
    ans = get_ans(q ,h , e, N, ct) 
    io.recvuntil("Give me your cake:") 
    io.sendline(str(ans)) 
    io.interactive() 
    io.close() 
e = make_cake() 
eat_cake(e) 
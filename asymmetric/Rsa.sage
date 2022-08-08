import gmpy2

#扩展维纳攻击，两个小解密指数，https://ctf-wiki.org/crypto/asymmetric/rsa/d_attacks/rsa_extending_wiener/#_2
def ex_wiener(e1,e2,n,e,c):
    D = diagonal_matrix(ZZ, [N, int(N^(1/2)), int(N^(1+a)), 1])
    M = matrix(ZZ, [[1, -N, 0, N^2], [0, e1, -e1, -e1*N], [0, 0, e2, -e2*N], [0, 0, 0, e1*e2]])*D
    L = M.LLL()
    t = vector(ZZ, L[0])
    x = t * M^(-1)
    phi = int(x[1]/x[0]*e1)
    d = gmpy2.invert(E,phi)
    print(d)
    m = pow(c,d,N)
    print(m)
    return m
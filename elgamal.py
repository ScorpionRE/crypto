import gmpy2
PK = 11496075768305337400615691305824078755552811953107530344393099165443081142499567126258295155973173746213213707843701733303043515285566768766635366352888223
#求g、q、SK


def decrypt(PK, SK, c):
    p = PK
    g, q = SK
    g_inv = gmpy2.invert(g, p)

    m = (c * pow(g_inv, 3, p) % p) % q
    return m


if __name__ == '__main__':
    from secret import flag
    assert flag.startswith('{') and flag.endswith('}')
    assert len(flag) == 34

    PK, SK = keygen()
    raw_flag = flag[1:-1]

    with open('data.txt', 'w') as f:
        f.write("PK: %d\n" % PK)
        for m in raw_flag:
            bit = int(m, 2)
            c = encrypt(PK, SK, bit)
            f.write(str(c) + '\n')

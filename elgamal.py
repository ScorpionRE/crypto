import gmpy2
#离散对数
import libnum
import sympy
from Crypto.Util.number import long_to_bytes

c = 6665851394203214245856789450723658632520816791621796775909766895233000234023642878786025644953797995373211308485605397024123180085924117610802485972584499
m = 391190709124527428959489662565274039318305952172936859403855079581402770986890308469084735451207885386318986881041563704825943945069343345307381099559075
n = 2**512
x = sympy.discrete_log(n,c,m)
print(long_to_bytes(x))
# PK = 11496075768305337400615691305824078755552811953107530344393099165443081142499567126258295155973173746213213707843701733303043515285566768766635366352888223
# #求g、q、SK
#
#
# def decrypt(PK, SK, c):
#     p = PK
#     g, q = SK
#     g_inv = gmpy2.invert(g, p)
#
#     m = (c * pow(g_inv, 3, p) % p) % q
#     return m
#
#
# if __name__ == '__main__':
#     from secret import flag
#     assert flag.startswith('{') and flag.endswith('}')
#     assert len(flag) == 34
#
#     PK, SK = keygen()
#     raw_flag = flag[1:-1]
#
#     with open('data.txt', 'w') as f:
#         f.write("PK: %d\n" % PK)
#         for m in raw_flag:
#             bit = int(m, 2)
#             c = encrypt(PK, SK, bit)
#             f.write(str(c) + '\n')

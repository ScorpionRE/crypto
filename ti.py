import itertools

import gmpy2
from Crypto.Util.number import long_to_bytes
from sympy import nthroot_mod
from sympy.ntheory.modular import crt

p = 107316975771284342108362954945096489708900302633734520943905283655283318535709
e = 256
c = 19384002358725759679198917686763310349050988223627625096050800369760484237557
#x**n = a mod p
m = nthroot_mod(c,256,p,all_roots=True)
print(m)
for i in m:
    print(long_to_bytes(i))



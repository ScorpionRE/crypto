import sympy
import math
#多元方程组

x = sympy.Symbol('x')
y = sympy.Symbol("y")
z = sympy.Symbol("z")
a = math.factorial(2020)
print(a)
print(hex(int(str(a)[:8])))

x = pow(520,1314) + pow(2333,666)
print(x)
print(hex(int(str(x)[:8])))

solved_value = sympy.solve([3*x-y+z-185,2*x+3*y-z-321,x+y+z-173 ],[x,y,z])
print(solved_value)
import sympy

#多元方程组

x = sympy.Symbol('x')
y = sympy.Symbol("y")
z = sympy.Symbol("z")


solved_value = sympy.solve([3*x-y+z-185,2*x+3*y-z-321,x+y+z-173 ],[x,y,z])
print(solved_value)
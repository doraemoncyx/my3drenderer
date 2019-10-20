import sympy

x0, y0, x1, y1, x2, y2 = sympy.symbols('x0,y0,x1,y1,x2,y2')
xp, yp = sympy.symbols('xp,yp')

m = sympy.Matrix([
	[x1 - x0, x2 - x0],
	[y1 - y0, y2 - y0]
])

uv: sympy.Matrix = m.inv(method='LU') * sympy.Matrix([xp - x0, yp - y0])
print(uv.shape)
print(sympy.simplify(uv))



out = sympy.Matrix([
	[((x0 - x2)*(y0 - yp) + (x0 - xp)*(-y0 + y2))/((x0 - x1)*(-y0 + y2) + (x0 - x2)*(y0 - y1))],
	[(-(x0 - x1)*(y0 - yp) + (x0 - xp)*(y0 - y1))/((x0 - x1)*(-y0 + y2) + (x0 - x2)*(y0 - y1))]
])
# print(sympy.factor(uv))
#
# data = [(x0, 276), (y0, 213), (x1, 276), (y1, 218), (x2, 282), (y2, 216), ]
# print(m.subs(data))
# m1 = sympy.simplify(m.inv(method='LU'))
# print(m1)
# print(m1.subs(data))
# print(uv.subs(data))
# print(m.subs(data).inv())
# print(m.inv().subs(data))
#
# m1 = sympy.Matrix([
# 	[0, 6],
# 	[5, 3]
# ]
# )
# print(m1.inv())

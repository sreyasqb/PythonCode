import sympy as sp
x= sp.symbols('x')
def taylorSeries(fx, x0, y0, x1):
    l = [y0]
    e=0
    for i in range(5):
        e = fx.diff(x)
        z=e.subs(x,0).subs(y,y0)
        print(e,z,sep=' // ')
        l.append(e)
    return l
y = sp.Function('y')(x)
print(taylorSeries(x**2 * y - 1, 0, 1, 0.1))

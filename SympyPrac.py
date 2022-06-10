
#question number 36

from sympy import *
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x,k1,k2=sp.symbols('x C1 C2')
f=sp.Function('f')(x)
eq=sp.Eq(f.diff(x,x)+5*f,0)
soln=sp.dsolve(eq).subs(k1,1).subs(k2,1)
func=lambdify(x,soln.rhs,'numpy')
xvals=np.arange(0,10,0.1)
yvals=func(xvals)
print(yvals)
plt.plot(xvals,yvals)
plt.show()



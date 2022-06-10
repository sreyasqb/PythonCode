import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
def q1():
    x, y = sp.symbols("x y")
    def solveOneVariable(s):
        s=sp.parse_expr(s.replace("=",','))
        print(sp.solve(s))


    def solveFactorise(s):
        s=sp.parse_expr(s.replace('=',','))
        print(sp.factor(s))

    def solveSubstitute(s,k):
        s=sp.parse_expr(s)
        print(s.subs(x,k))

    def solveTwoVariable(s1,s2):
        s1=sp.Eq(sp.parse_expr(s1),0)
        s2=sp.Eq(sp.parse_expr(s2),0)
        ans=sp.solve((s1,s2),(x,y))
        print(ans)



    def expressions():
        n=int(input("Enter no of expressions :"))# taking input from user

        for i in range(1,n+1):

            choice=int(input("1.Solve one variable linear Equation or Non linear equation\n"
                             "2.Solve two Variable Non linear Equation\n"
                             "3.Factorise the equation\n"
                             "4.Substitute value in the equation : "))
            print()
            if choice==1:
                try:
                    a=input("Enter the expresion in this format \n eg: 2*x+1=0 or x**2+3*x+4=0\n Enter : ")
                    solveOneVariable(a)
                except:
                    print("Invalid input")

            if choice==2:
                try:
                    a=input("Enter linear eq 1 in the format\neg: x+3*y-1 : ")
                    b = input("Enter linear eq 1 in the format\neg: 2*x+y+4 : ")
                    solveTwoVariable(a,b)
                except:
                    print("invalid input")


            if choice==3:
                try:
                    a = input("Enter the expresion in this format \n eg: x**2+2*x+1 or x**2+5*x+6\n Enter : ")
                    solveFactorise(a)
                except:
                    print("Invalid input")

            if choice==4:
                try:
                    a = input("Enter the expresion in this format \n eg: x**3+2*x+1 or x**2+5*x-1\n Enter : ")
                    k=float(input("Enter the value to substitute for x : "))
                    solveSubstitute(a,k)
                except :
                    print("Invalid input")







    expressions()


q1()

def q2():
    xvals=np.arange(0,10,0.1)
    y1vals=(np.e**(-xvals/10))*np.sin(np.pi*xvals)
    y2vals=xvals*(np.e**(-xvals/3))

    plt.plot(xvals,y1vals,label="e^(-x/10) * sin(pi*x)")
    plt.plot(xvals,y2vals,label="x * e^(-x/3)")
    plt.xlabel("X AXIS")
    plt.ylabel("Y AXIS")
    plt.legend()
    plt.show()

#q2()

def q3():
    size1=eval(input("Enter AMAT size in list format eg: [2,3] : "))
    size2 = eval(input("Enter BMAT size in list format : "))
    print("AMAT INPUT : ")
    amat=np.array([float(input("Enter row "+str(i)+" column "+str(j)+" : ")) for i in range(1,size1[0]+1) for j in range(1,size1[1]+1)]).reshape(size1)
    print("BMAT INPUT : ")
    bmat = np.array(
        [float(input("Enter row " + str(i) + " column " + str(j) + " : ")) for i in range(1, size2[0] + 1) for j in
         range(1, size2[1] + 1)]).reshape(size2)
    print("AMAT IS : \n",amat)
    print("BMAT IS : \n",bmat)
    print("Rank of AMAT is :",np.linalg.matrix_rank(amat),
          ",Rank of BMAT is :",np.linalg.matrix_rank(bmat))
    print("Sum of the matrices is :\n",amat+bmat)
    print("Product of the matrices is :\n",np.matmul(amat,bmat))
    print("Division of the matrices amat/bmat is :\n",np.divide(amat,bmat))
    print("The transpose of AMAT IS :\n",amat.transpose(),"\nThe transpose of BMAT is :\n",bmat.transpose())
    print("The inverse of AMAT IS :\n", np.linalg.inv(amat), "\nThe inverse of BMAT is :\n",np.linalg.inv(bmat))
    k=int(input("Enter the scalar u want to multiply AMAT with : "))
    print("SCALAR PRODUCT IS : \n",k*amat)
#q3()




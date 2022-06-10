def f1():
    l=[1,2,1,11,2,12,10,9,8]
    print(l,[i if i<10 else 10 for i in l],sep='\n')

def f2():
    l=["Hello","hi","bye"]
    print(l,[i[1:] for i in l],sep='\n')
#f2()
def f3():
    print([i for i in range(50)],[i**2 for i in range(1,51)],[chr(i)*(i-96) for i in range(97,123)],sep='\n')
#f3()
def f4():
    L=[1,2,3]
    M=[6,7,8]
    print(L,M,[L[i]+M[i] for i in range(len(M))],sep='\n')
#f4()
def f5():
    n=int(input("Enter :"))
    print([i for i in range(1,n//2+1) if n%i==0 ]+[n])
#f5()
def f6():
    n=int(input("Enter number upto 12 :"))
    print("The probability of getting ",n,"is",(n-1)/36*100 if n<8 else (13-n)/36*100)
#f6()
def f7():
    l=[1,2,3,4,5,9,1,2]
    print(l,[l[-1] if i==-2 else l[i+1] for i in range(-2,len(l)-2)],sep='\n')
#f7()
def f8():
    l,z=[str(int(10**i)) for i in range(11)],[]
    for i in l:
       z+=[*i]
    print(list(map(int,z))+[1])
#f8()
def f9():
    import random
    l=[random.randint(0,1) for i in range(100)]
    s,max=0,0
    for i in range(len(l)):
        if l[i]==0: s+=1
        else:
            if s>max:
                max=s
            s=0
    print(l,max if s==0 else (max if s<max else s),sep='\n')
#f8()
def f10():
    l=[1,2,1,2,0,0,0,3,3,3]
    print(list(set(l)))
#()
def f11():
    n=float(input("Enter length in feet :"))
    d={1:12*n,2:0.33*n,3:0.00019*n,4:n*304.8,5:n*30.48,6:n*0.30,7:0.00030}
    print(str(n)+" feet ",d[int(input("1->inches ,2->yards,3->miles,4->mm,5->cm,6->m,7->km :"))],sep='------>>>')
#f11()
print("The output for the 1st ques is: ")
f1()
print("The output for the 2nd ques is: ")
f2()
print("The output for the 3rd ques is: ")
f3()
print("The output for the 4th ques is: ")
f4()
print("The output for the 5th ques is: ")
f5()
print("The output for the 6th ques is: ")
f6()
print("The output for the 7th ques is: ")
f7()
print("The output for the 8th ques is: ")
f8()
print("The output for the 9th ques is: ")
f9()
print("The output for the 10th ques is: ")
f10()
print("The output for the 11th ques is: ")
f11()










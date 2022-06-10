import re
# x=1234
# print(sum(map(lambda i : int(i)**len(str(x)),list(str(x)))))
#factorial one liner
def sum(n):
    if n==1:
        return 1
    else:
        n+sum(n-1)
# x=lambda i : 1 if i<=1 else i*x(i-1)
# print(x(5))
y=lambda n: 0 if n<=0 else n+y(n-1)
print(y(4))

l=[1,2,3,4]

#print(l)
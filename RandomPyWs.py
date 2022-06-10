l=[1,2,3,4,5]
m=list(l)
m.sort()
print(len(l),l[-1],l[::-1],"yes" if 5 in l else "no",l.count(5),sep=" / ")
if 5 in l:
    print("yes")
else:
    print("no")
l=l[1:len(l)-2]
l.sort()
print(l,m.index(5),sep="/ ")

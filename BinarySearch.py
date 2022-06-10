l=[1,2,3,4,5,6,7,8]
key=4
def BinSearch(a,b):
    if l[a]==key:
        print(a)
    elif l[b-1]==key:
        print(b-1)

    if l[(a+b)//2]>key:
        BinSearch(a,(a+b)//2)
    elif l[(a+b)//2]<key:
        BinSearch((a+b)//2,b)



BinSearch(0,len(l))


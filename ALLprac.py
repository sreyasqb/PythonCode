def q1():
    b1=0
    b2=0
    print("b1 and b2 is : "+str(b1*b2))
    print("b1 or b2 is : ",1 if b1+b2>0 else 0)
    print("Not of b1 :",(b1+1)%2 ,"not of b2 is :",(b2+1)%2)

# q1()
def q2():
    n=16
    bn=n
    on=n
    hn=n
    bs=''
    os=''
    hs=''
    while bn:
        bs+=str(bn%2)
        bn//=2
    print("binary is : ",bs[::-1])
    while on:
        os+=str(on%8)
        on//=8
    print("Octal is : ",os[::-1])
    while hn:
        if (hn%16>9):
            hs+=chr(ord('A')+(hn%16-10))
        else:
            hs+=str(hn%16)
        hn//=16
    print("Hexadecimal is :",hs[::-1])

    hextodec="8F"
    bintodec="10111"
    binn=0
    octtodec="723"
    octn=0
    hexn=0
    for i in range(len(bintodec)):
        binn+=int(bintodec[i])*2**(len(bintodec)-i-1)
    print("Binary to dec is : ",binn)
    for i in range(len(octtodec)):
        octn+=int(octtodec[i])*8**(len(octtodec)-i-1)
    print("Octal to dec is : ",octn)
    for i in range(len(hextodec)):
        temp=hextodec[i]
        if hextodec[i].isalpha():
            temp=ord(temp)-ord('A')+10
            hexn+=temp*16**(len(hextodec)-i-1)
        else:
            hexn += int(hextodec[i]) * 16 ** (len(hextodec) - i - 1)
    print("hex to dec is :",hexn)

#q2()

def q3():
    n=list("1110000")
    print("the original number is :",*n)
    for i in range(len(n)):
        n[i]=(int(n[i])+1)%2
    print("Ones compliment is : ",*n)
    for i in range(len(n)-1,-1,-1):
        if n[i]!=1:
            n[i]=1
            break
        else:
            n[i]=0
    else:
        n=[1]+n
    print("two's complement is : ",*n)





q3()






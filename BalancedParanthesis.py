
def balanced_parens(s):
    d={'}':'{',']':'[',')':'('}
    l=[s[0]]
    i=1
    j=0
    while i<len(s):
        if s[i] in ['(','{','[']:
            l.append(s[i])
        elif s[i] in [')','}',']']:
            if s[i-1]==d[s[i]]:
                l.pop(i-1)
                i-=2

        print(l,s,sep="////")
        i+=1

    print("Correct paranthesis" if l==[] else "Incorrect")


print(balanced_parens(list("({})[])")))

def clearPrevious(alphabets,index):
    s=0
    for i in range(26):
        if alphabets[i]<=index and alphabets[i]!=-1:
            alphabets[i]=-1
            s+=1
    return s

def f(s):
    n=len(s)
    alphabets=[-1 for i in range(26)]
    maxCount=0
    count=0
    for i in range(n):
        index=ord(s[i])-97
        if alphabets[index]==-1:
            alphabets[index]=i
            count+=1
        else:
            dec=clearPrevious(alphabets,alphabets[index])
            alphabets[index]=i
            if count>maxCount:
                maxCount=count
            count-=dec-1
        # print(alphabets,count)
    # print(maxCount)
    return maxCount
s='pwwkew'
f(s)

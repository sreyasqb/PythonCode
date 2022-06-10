l=[]

def combination(word,n):
    if len(word)==1:
        return [word]
    char=word[0]

    word=word[1:]

    for i in range(len(word)) :
        word[i]=char+word[i]
    print(word)
    if len(word)>N-n:
        combination(word,n)
    return word

word=["a","b","c","d","e"]
N=len(word)
n=3
print(combination(word,n))



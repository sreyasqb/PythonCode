def permutation(l):
    if len(l)==1:
        return [l]
    perms=permutation(l[1:])
    char=l[0]
    result=[]
    for perm in perms:
        for i in range(len(perms)+1):
            result.append(perm[:i]+char+perm[i:])
    return result
print(set(permutation("abc")))






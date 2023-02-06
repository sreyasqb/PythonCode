l=[10,9,2,5,4,7,101,87]
n=len(l)
i=0
j=0
count=[1 for i in range(n)]
while i<n and j<n:
    print(i,j,count)
    if j>=i and i<n-1:
        j=0
        i+=1
    if l[j]<l[i]:
        count[i]=max(count[j]+1,count[i])
    j+=1
print(count)    
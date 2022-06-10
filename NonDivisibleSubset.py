def nonDivisibleSubset(l,n,k):
    count_list=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if (l[i]+l[j])%k!=0:
                print(l[i],l[j])
                count_list[i]+=1
                count_list[j]+=1
    count_list.sort(reverse=True)
    print(count_list)
    var=0
    # while  True:
        
nonDivisibleSubset([1,7,2,4],4,3)                


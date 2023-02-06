l=[7,7,7,7,3,5,7,5,3]

def majorityElement(nums):
    n=len(nums)
    d={}
    for i in nums:
        if i in d:
            if d[i]>n/2-1:
                return i
            d[i]+=1
        else:
            d[i]=1

    


print(majorityElement(l))
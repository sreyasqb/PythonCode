import math
nums=[1,2,3,4]
#15267

def minPositive(nums):
    n=len(nums)
    found1=False
    for i in range(n):
        if nums[i]<0 or nums[i]>n:nums[i]=0
        if nums[i]==1:found1=True
    if not found1:return 1
    print(nums)
    for i in range(n):
        x=nums[i]
        nums[x],nums[i]=nums[i],nums[x]        

    st=nums[0]   
    print(nums) 
    for i in range(n-1):
        if nums[i]!=0 and nums[i]!=st+1:
            return st+1
        elif nums[i]==st+1:
            st+=1

    # print(nums)
            
print(minPositive(nums))
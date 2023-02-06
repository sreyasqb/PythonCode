from collections import deque
def slidingWindowMax(nums,k):
    q=deque([nums[0]])
    qSize=1
    for i in range(1,k):
        if nums[i]>q[-1]:
            j=qSize
            while qSize>0 and nums[j]:
                pass





l=[1,3,-1,-3,5,3,6,7]
k=3
slidingWindowMax(l,k)
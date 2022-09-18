def pattern1(n):
    for i in range(1,2*n+1,2):
        for j in range(n*2-1):
            if i<=n and ((n//2-(i-1)//2-1<j<n//2+(i-1)//2+1) or (n-1 + n//2-(i-1)//2-1 < j < n-1 + n//2+(i-1)//2+1)): #7-2 + 3 - 1-1
                print(i,end='')
            elif i>n and ((n//2 - (n*2-i-1) // 2 - 1< j < n//2 + (n*2-i-1)//2 + 1) or (n-1 + n//2 - (n*2-i-1) // 2 - 1< j < n-1 + n//2 + (n*2-i-1)//2 + 1)):
                print(n*2-i,end='')
            else:
                print(' ',end='')          
        print()
pattern1(17)

#1-3,9
#2-2,3,4 8,9,10
#3 -> 1,2,3,4  
#5 -> 1,2,3,4 6,7,8,9


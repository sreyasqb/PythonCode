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
# pattern1(5)




def pattern2(n):
    l=[0]
    t=0
    s=1
    for i in range(n*(n+1)//2):
        l.append(bin(s)[2:])
        m=t
        t=s
        s+=m
    
    x=0
    for i in range(n):
        for j in range(n):
            if j<=i:
                print(l[x],end=' ')
                x+=1
            else:
                print(' ',end='')
        print()
# pattern2(6)
def pattern3(n):
    for i in range(n):
        for j in range(2*n-1):
            if j<n and (i==0 or i==n-1):
                print('*',end=' ')
            elif (0<i<n-1) and (j==0 or j==2*n-4 or j==2*i-1):
                print('*',end=' ')
            else:
                print(end=' ')                
        print()
    


pattern3(7)


# def pattern4():
#     for i in range(1,10):
#         for j in range(1,10):
#             if i==j or i+j==10:
#                 print('*',end=' ')
#             else:
#                 print(end=' ')
#         print()

# pattern4()
# n=int(input('Enter no of lines : '))
# pattern2(n)




#1-3,9
#2-2,3,4 8,9,10
#3 -> 1,2,3,4  
#5 -> 1,2,3,4 6,7,8,9


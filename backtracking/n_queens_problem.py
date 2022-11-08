class Queen:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def setPosition(self,x,y):
        self.x=x
        self.y=y
    
    def nextPosition(self,arr,n):
        arr=arr[:-1]
        print(f'q : {self} ')
        for j in range(self.y+1,n):
            self.y=j
            if not self.checkAttackList(self,arr):
                print(f'fq : {self}')
                return True
        return False
    
    def nextColumn(self,n):
        if self.y+1<n:
            self.y+=1
            return True
        return False

    @classmethod
    def checkAttack(cls,q1,q2):
        return True if q1.x==q2.x or q1.y==q2.y or (abs(q1.x-q2.x)==1 and abs(q1.y-q2.y)==1) else False #diagonal
    @classmethod
    def checkAttackList(cls,q,arr):
        for queen in arr:
            if cls.checkAttack(q,queen):return True
        return False

    def __str__(self):
        return f'({self.x},{self.y})'

def nQueens(n):
    queens=[Queen(0,0)]
    c=0
    while c<1:
        i=1
        while i<n:
            queen=Queen(i,0)
            # print(f'i : {i}')
            for j in range(n):
                queen.setPosition(i,j)
                if not Queen.checkAttackList(queen,queens):
                    queens.append(queen)
                    break
            else:
                i-=1
                if queens[-1].nextColumn(n)==False:
                    print('hi')
                    queens.pop()
                    i-=1
                else:
                    if queens[-1].nextPosition(queens,n)==False:
                        queens.pop()
                        i-=1
                    
                    
                  
                   
                
            for q in queens:
                print(q)
            print('-----')
            i+=1
                
        c+=1
    
    

nQueens(4)

# class Test:
#     def __init__(self,x):
#         self.x=x

# l=[Test(1),Test(2)]
# print(l[-1].x)
# b=l[-1]
# b.x=5
# print(l[-1].x)
# l=[1,2,3,4]
# print(l[:-1])

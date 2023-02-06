class Queen:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    @classmethod
    def checkAttack(cls,l,x,y):
        for queen in l:
            if queen.x==x or queen.y==y or abs(queen.x-x)==abs(queen.y-y):
                return True
        return False
    
    @classmethod
    def reassign(cls,l,n,i):
        if l[-1].y<n-1:
            l[-1].y+=1
            if cls.checkAttack(l[1:-1],l[-1].x,l[-1].y)==False:
                return (l,i)
            else:
                cls.reassign(l,n,i)
        else:
            l.pop()
            return cls.reassign(l,n,i-1)
    def __str__(self):
        return f'({self.x},{self.y})'
    def __repr__(self):
        return f'({self.x},{self.y})'

def nQueens(n):
    assigned=[Queen(0,0)]
    i=1
    while assigned[0].y!=n-1:
        check=True
        for j in range(n):
            check=Queen.checkAttack(assigned,i,j)
            if check==False:
                assigned.append(Queen(i,j))
                i+=1
                break
        if check:
            assigned,i=Queen.reassign(assigned,n,i)
        if i==n:
            print(assigned)
            # assigned.pop()
            # i-=1
            # assigned,i=Queen.reassign(assigned,n,i)
            break

        

nQueens(8)
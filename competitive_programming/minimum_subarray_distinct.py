class Solution:
    
    def orangesRotting(self, grid) -> int:
        rotten=[]
        m = len(grid)
        n = len(grid[0])
        totalOrange=0
        rottenOrange=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    totalOrange+=1
                elif grid[i][j]==2:
                    totalOrange+=1
                    rottenOrange+=1
                    rotten.append((i,j))
        minutes=0
        while rottenOrange<totalOrange:
            temp = []
            changeCount=0
            for x,y in rotten:
                for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if 0<=i+x<m and 0<=j+y<n and grid[i+x][j+y]==1:
                        temp.append((i+x,j+y))
                        grid[i+x][j+y] = 2
                        rottenOrange+=1
                        changeCount+=1
            if changeCount==0 : return -1
            rotten = temp
            minutes+=1
            print(rotten)
        print(minutes)
sol = Solution()
print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
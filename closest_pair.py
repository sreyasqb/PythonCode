def distance(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

pair=[]
def closestPair(points:list):
    global pair
    n=len(points)
    if n == 2:
        a,b=points
        return distance(a,b)
    if n==1:
        return 100000
    
    dl=closestPair(points[:n//2])
    dr=closestPair(points[n//2:])
    d=min(dl,dr)

    pointsY=sorted(points,key=lambda x:x[1])
    for i in range(n):
        for j in range(i+1,i+8):
            if i+j < n :
                d=min(d,distance(pointsY[i],pointsY[i+j]))
                pair=[pointsY[i],pointsY[i+j]]
    return d

points = [
            (2, 2), # A
            (2, 8), # B
            (5, 5), # C
            (6, 3), # D
            (6, 7), # E
            (7, 4), # F
            (7, 9)  # G
]

print(closestPair(sorted(points,key=lambda x:x[0])))
print(pair)
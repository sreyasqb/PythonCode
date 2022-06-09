graph={
    'A':{'B':6,'D':1},
    'B':{'A':6,'C':5,'E':2,'D':2},
    'C':{'B':5,'E':5},
    'D':{'A':1,'B':2,'E':1},
    'E':{'B':2,'C':5,'D':1}
}
vertices=list(graph.keys())
source='A'
distance={}
visited=[]
for v in vertices:
    if v==source : distance[v]=0
    else : distance[v]=float('inf')
print(distance)
print(vertices)
i=0
while len(visited)!=len(vertices)-1:
    nextSource,minDist='',float('inf')
    for v in graph[source]:
        if graph[source][v]+distance[source]<distance[v] and v not in visited:
            distance[v]=graph[source][v]+distance[source]
            if distance[v]<minDist:
                nextSource=v
                minDist=distance[v]
    visited.append(source)
    source=nextSource
    print(distance)
    # print(visited)



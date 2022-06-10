graph={
    'A':{'B':6,'D':1},
    'B':{'A':6,'C':5,'E':2,'D':2},
    'C':{'B':5,'E':5},
    'D':{'A':1,'B':2,'E':1},
    'E':{'B':2,'C':5,'D':1}
}
vertices=list(graph.keys())
orSource='A'
source='A'
distance={}
visited=[]
for v in vertices:
    if v==source :
        distance[v]={"dist":0,"prev":source}
    else :
        distance[v]={"dist":float('inf'),"prev":''}
# print(distance)
# print(vertices)
i=0
while len(visited)!=len(vertices)-1:
    nextSource,minDist='',float('inf')
    for v in graph[source]:
        if graph[source][v]+distance[source]["dist"]<distance[v]["dist"] and v not in visited:
            distance[v]["dist"]=graph[source][v]+distance[source]["dist"]
            distance[v]["prev"]=source
            if distance[v]["dist"]<minDist:
                nextSource=v
                minDist=distance[v]["dist"]
    visited.append(source)
    source=nextSource
    # print(distance)
    # print(visited)
print(distance)
dest='E'
path=[]
while dest!=orSource:
    path.append(dest)
    # print(distance[dest]["prev"])
    dest=distance[dest]["prev"]
path=(path+[orSource])[::-1]
print(path)





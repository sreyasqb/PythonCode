

def findPartion():
    graph={}
    data=[[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]
    n=9
    for i in data:
        x,y=i
        if x not in graph:
            graph[x]=[y]
        else:
            graph[x].append(y)
        if y not in graph:
            graph[y]=[x]
        else:
            graph[y].append(x)

    colors={}
    for i in range(1,n+1):
        print(graph,colors)
        if i not in colors:
            colors[i]=0
            for j in graph[i]:
                if j in colors and colors[j]==0:
                    return False
                colors[j]=1
        else:
            for j in graph[i]:
                if j in colors and colors[j]==colors[i]:
                    return False
                colors[j]=0 if colors[i]==1 else 1
    return True
        
print(findPartion())   


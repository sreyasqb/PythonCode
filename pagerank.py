def printDict(d):
    for key in d:
        print(f'{key} : {d[key]}')
graph={
    'A':['B','C'],
    'B':['D'],
    'C':['A','B','D'],
    'D':['C'],
}
n=len(graph)
prob={}
for i in graph:
    prob[i]=1/n
print('ITERATION 0')
printDict(prob)
print()
probDup=dict(prob)
i=1
while True:
    for v in graph:
        s=0
        for w in graph:
            if v in graph[w]:
                s+=prob[w]/len(graph[w])
        probDup[v]=s
    prob=dict(probDup)
    print(f'ITERATION {i}')
    printDict(prob)
    print()
    i+=1
    if i>15:
        break



# print(sum(l))



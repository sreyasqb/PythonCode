def q7():
    f=open("D:\\RandomSoftware\\abc.txt")
    l=f.read().split()
    #d={i:l.count(i) for i in l}
    d={}
    for i in l:
        d[i]=l.count(i)
    maxvalue=max(d.values())
    b=list(d.values()).index(maxvalue)
    word=list(d.keys())[b]
    print("no of times is ",maxvalue,"word is",word)
    #print([[max(d.values()),i] for i in d if d[i]==max(d.values())])


def q8():
    f = open("D:\\RandomSoftware\\abc.txt")
    s=f.read()
    for i in s:
        pass
def q12():
    l = [1, 2, 3]
    def push(v):
        l.append(v)
    def Pop():
        l.pop()
    def display():
        print(l)
    while True:
        n=int(input("1-push,2-pop,3-disp,0-exit:"))
        if n==1:
            a=int(input("Enter value:"))
            push(a)
        elif n==2:
            l.pop()
        elif n==3:
            display()
        elif n==0:
            break
q12()
def q11():
    import csv
    data_list = [["SN", "Name", "Contribution"],
                 [1, "Linus Torvalds", "Linux Kernel"],
                 [2, "Tim Berners-Lee", "World Wide Web"],
                 [3, "Guido van Rossum", "Python Programming"]]
    with open('innovators.csv', 'w', newline='') as file:
        writer = csv.writer(file,


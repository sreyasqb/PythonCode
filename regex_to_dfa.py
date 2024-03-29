from enum import Enum

#TREAT FOR GETTING PLACED

class Operator(Enum):
    CONCATINATION = 1
    OR = 2
    CLOSURE = 3
    TERMINAL = 4

class Node:
    def __init__(self,type,val,left=None,right=None):
        self.type = type
        self.val = val
        self.left = left
        self.right = right
        self.first = set()
        self.follow = set()
        self.last = set()
        self.nullable = False
        
    def __str__(self):
        return f'type : {self.type} - val : {self.val}'
    

#s = 'a.(b+c)*#'
# s = '(a+b)*.a.b.b'
s = 'a.(a+b)*.b.b'

#

def priority(c):
    if c=='*':return 2
    elif c=='.':return 1
    elif c=='+':return 0
    return -1

isTerminal = lambda x:True if ord('a')<=ord(x)<=ord('z') else False
terminals = set()
def postfix(s):
    ans = ''
    l = []
    for i in range(len(s)):
        if isTerminal(s[i]):
            ans+=s[i]
            terminals.add(s[i])
        elif len(l)==0 or s[i]=='(':
            l.append(s[i])
        elif s[i]==')':
            while l[-1]!='(':
                ans+=l.pop()
            l.pop()
        elif s[i] in ['+','.','*']:
            while len(l)!=0 and priority(s[i])<priority(l[-1]):
                ans+=l.pop()
            l.append(s[i])
    while len(l)!=0:
        ans+=l.pop()
    return ans

print(postfix(s))

def constructParseTree(s):
    s = postfix(s)
    i=0
    #print(s)
    stack = []
    terminalCount,concatCount,orCount,closureCount = 1,1,1,1

    while i<len(s):
        if isTerminal(s[i]):
            terminal = Node(Operator.TERMINAL,(terminalCount,s[i]))
            stack.append(terminal)
            terminalCount+=1
        elif s[i] in '+':
            operator = Node(Operator.OR ,(orCount,s[i]),left = stack[-2],right = stack[-1])
            stack.pop()
            stack.pop()
            stack.append(operator)
            orCount+=1
        elif s[i] == '.':
            operator = Node(Operator.CONCATINATION,(concatCount,s[i]),left = stack[-2],right = stack[-1])
            # operator = Node(Operator.CONCATINATION,f'{s[i]}{concatCount}',left = stack[-2],right = stack[-1])
            stack.pop()
            stack.pop()
            stack.append(operator)
            concatCount+=1
        elif s[i]=='*':
            operator = Node(Operator.CLOSURE,(closureCount,s[i]),left = stack[-1])
            # operator = Node(Operator.CLOSURE,f'{s[i]}{closureCount}',left = stack[-1])
            stack[-1] = operator
            closureCount+=1
        #print(stack)
        i+=1
    root = stack[0]
    rightHash = Node(Operator.TERMINAL,(terminalCount,'#'))
    tempRoot = Node(Operator.CONCATINATION,f'.{concatCount}',left=root,right=rightHash)
    return tempRoot
    # print(root.left,root.right)
    # print(root.left.left.right)

root = constructParseTree(s)

follow = {}
def dfs(root):
    global initialState
    if not root:return
    firstVals = list(map(lambda x:x.val,root.first))
    lastVals = list(map(lambda x:x.val,root.last))
    followVals = list(map(lambda x:x.val[0],root.follow))
    print(root.val,root.nullable,firstVals,lastVals,followVals,sep = '\t')
    if root.type == Operator.TERMINAL:
        # head = root.val.rstrip('0123456789')
        # tail = root.val[len(head):]
        follow[root.val] = set(followVals)
    
        
    dfs(root.left)
    dfs(root.right)

def dfsNullable(root):
    if not root : return 
    dfsNullable(root.left)
    dfsNullable(root.right)
    if root.type==Operator.CLOSURE : root.nullable = True
dfsNullable(root)

def dfsFirst(root):
    if not root : return
    dfsFirst(root.left)
    dfsFirst(root.right)
    if root.type==Operator.TERMINAL:
        root.first.add(root)
    elif root.type==Operator.CONCATINATION:
        if not root.left.nullable:
            root.first = root.left.first
        else:
            root.first =  root.left.first | root.right.first
    elif root.type in [Operator.CLOSURE,Operator.OR]:
        rightSet = set() if root.right==None else root.right.first
        root.first = root.left.first | rightSet

def dfsLast(root):
    if not root:return
    dfsLast(root.left)
    dfsLast(root.right)
    if root.type==Operator.TERMINAL:
        root.last.add(root)
    elif root.type==Operator.CONCATINATION:
        if root.right.nullable:
            root.last = root.left.last | root.right.last
        else:
            root.last = root.right.last
    elif root.type in [Operator.CLOSURE,Operator.OR]:
        rightSet = set() if root.right==None else root.right.last
        root.last = root.left.last | rightSet

def dfsFollow(root):
    if not root:return
    dfsFollow(root.left)
    dfsFollow(root.right)
    if root.type==Operator.CLOSURE:
        for node in root.last:
            node.follow = node.follow | root.first
    if root.type == Operator.CONCATINATION:
        for node in root.left.last:
            node.follow = node.follow | root.right.first


dfsFirst(root)      
dfsLast(root)
dfsFollow(root)
print('Symbol','Nullable','First','Last','Follow',sep = '\t')
dfs(root)
# print(follow)

initalState = tuple(sorted((map(lambda x:x.val[0],root.first))))
# print(initalState)

dfa = {initalState:{}}
queue = [initalState]


# print(terminals)

def constructDfa():
    while len(queue)!=0:
        # print('queue : ',queue)
        newState = {queue[0]:{k:set() for k in terminals}}
        for state in queue[0]:
            for i in follow:
                if state == i[0] and i[1]!='#':
                    newState[queue[0]][i[1]] |= follow[i]
        for x in newState[queue[0]].values():
            if tuple(x) not in dfa:
                queue.append(tuple(x))
                dfa[tuple(x)] = {}
        # print('queue ',queue)
        # print(newState)
        
        dfa[queue[0]] = newState[queue[0]]
        queue.pop(0)
        # print('updated queue : ',queue)
    # print('dfa : ',dfa)

constructDfa()
print('\ndfa is : \n')
print(dfa)




#print(root.left,root.right,sep = ' <---> ')
# print(root.left.left.right)


        



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
s = '(a+b)*.a.b.b'

def priority(c):
    if c=='*':return 2
    elif c=='.':return 1
    elif c=='+':return 0
    return -1

isTerminal = lambda x:True if ord('a')<=ord(x)<=ord('z') else False

def postfix(s):
    ans = ''
    l = []
    
    for i in range(len(s)):
        if isTerminal(s[i]):
            ans+=s[i]
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


def constructParseTree(s):
    s = postfix(s)
    i=0
    #print(s)
    stack = []
    terminalCount,concatCount,orCount,closureCount = 1,1,1,1

    while i<len(s):
        if isTerminal(s[i]):
            terminal = Node(Operator.TERMINAL,f'{s[i]}{terminalCount}')
            stack.append(terminal)
            terminalCount+=1
        elif s[i] in '+':
            operator = Node(Operator.OR ,f'{s[i]}{orCount}',left = stack[-2],right = stack[-1])
            stack.pop()
            stack.pop()
            stack.append(operator)
            orCount+=1
        elif s[i] == '.':
            operator = Node(Operator.CONCATINATION,f'{s[i]}{concatCount}',left = stack[-2],right = stack[-1])
            stack.pop()
            stack.pop()
            stack.append(operator)
            concatCount+=1
        elif s[i]=='*':
            operator = Node(Operator.CLOSURE,f'{s[i]}{closureCount}',left = stack[-1])
            stack[-1] = operator
            closureCount+=1
        #print(stack)
        i+=1
    root = stack[0]
    rightHash = Node(Operator.TERMINAL,f'#{terminalCount}')
    tempRoot = Node(Operator.CONCATINATION,f'.{concatCount}',left=root,right=rightHash)
    return tempRoot
    # print(root.left,root.right)
    # print(root.left.left.right)

root = constructParseTree(s)


def dfs(root):
    if not root:return

    firstVals = list(map(lambda x:x.val,root.first))
    lastVals = list(map(lambda x:x.val,root.last))
    followVals = list(map(lambda x:x.val,root.follow))
    print(root.val,root.nullable,firstVals,lastVals,followVals,sep = '\t')
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
#print(root.left,root.right,sep = ' <---> ')
# print(root.left.left.right)


        



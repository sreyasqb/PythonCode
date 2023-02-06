class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    


root=Node(1)
root.left=Node(2)
root.right=Node(3)
# root.left.left=Node(5)
# root.left.right=Node(6)
root.right.left=Node(4)
root.right.right=Node(7)

def levelOrder(queue):
    newQueue=[]
    if len(queue)==0:
        return 'done' 
    
    print(queue[0].data)

    for node in queue:
        if node.left!=None:
            newQueue.append(node.left)
        if node.right!=None:
            newQueue.append(node.right)
    levelOrder(newQueue)
levelOrder([root]) 




    

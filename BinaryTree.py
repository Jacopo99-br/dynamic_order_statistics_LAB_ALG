import random
from collections import deque


#GLOBAL
index=0
select=[None,None]
value=None

class Node():
    def __init__(self,key=None,left=None,right=None,parent=None):
        self.key=key
        self.left=left
        self.right=right
        self.parent=parent

    # def left(self,left):
    #     self.left=left
    # def right(self,right):
    #     self.thisNode[2]=right
    # def key(self,key):
    #     self.thisNode[0]=key
    # def parent(self,parent):
    #     self.thisNode[3]=parent



class BinaryTree():

    elements=[None]
    list_key=[]
    nodes=[]
    
    # def insert(self,z_key):
    #     z=Node(z_key)
    #     y=None
    #     x=self.elements[0] #tree root

    #     while x!=None:
    #         y=x
    #         if z.thisNode[0]<x.thisNode[0]:
    #             x=x.thisNode[1]
    #         else:
    #             x=x.thisNode[2]
    #     z.thisNode[3]=y

    #     if y==None:
    #         self.elements.append(z) #l'albero era vuoto e z diventa la radice
    #     elif z.thisNode[0]<y.thisNode[0]:
    #         y.thisNode[1]=z
    #     else:
    #         y.thisNode[2]=z

    def insert(self,z_key):
        z=Node(z_key)
        y=None
        x=self.elements[0] #tree root

        while x!=None:
            y=x
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        z.parent=y

        if y==None:
            self.elements[0]=z #l'albero era vuoto e z diventa la radice
        elif z.key<y.key:
            y.left=z
        else:
            y.right=z

        self.nodes.append(z)

    def showTreeInorder(self,start):   #per stampare le chiavi dell'albero parentesizzato
        if start!=None:
            self.showTreeInorder(start.left)
            print(start.key)
            self.showTreeInorder(start.right)

    def TreeSearch(self,start,k): #mi restituisce l'albero dal nodo che ho cercato
        while start!=None and k!=start.key:
            if k<start.key:
                start=start.left
            else:
                start=start.right
        return start
    
    def Min(self,start):
        while start.left!=None:
            start=start.left
        return start
    
    def Max(self,start):
        while start.right!=None:
            start=start.right
        return start
    
    def tree_OS_Select(self,tree,i):
        global index
        index=0
        OS_Select(tree,i)

    def tree_OS_Rank(self,tree,i):
        global index
        index=0
        OS_Rank(tree,i)

    def tree_key_list(self,start):
        if start!=None:
            self.tree_key_list(start.left)
            self.list_key.append(start.key)
            self.tree_key_list(start.right)

    

def OS_Rank(node,i): 
    global index
    global select
    global value
    index=0
     # create an empty stack
    stack = deque()
 
    # start from the root node (set current node to the root node)
    curr = node
 
    # if the current node is None and the stack is also empty, we are done
    while stack or curr:
 
        # if the current node exists, push it into the stack (defer it)
        # and move to its left child
        if curr:
            stack.append(curr)
            curr = curr.left
        
        else:
            # otherwise, if the current node is None, pop an element from the stack,
            # print it, and finally set the current node to its right child
            curr = stack.pop()
            
            if curr.key==i:
                select[0]=index
                select[1]=curr
            index+=1
            curr = curr.right

    """ if node!=None:
                      
            OS_Rank(node.left,i)
            index+=1
            value=node.key
            if i==node.key:
                select[0]=index
                select[1]=node
            OS_Rank(node.right,i)
 """
def OS_Select(node,i): 
    global index
    global select
    global value

    index=0
     # create an empty stack
    stack = deque()
 
    # start from the root node (set current node to the root node)
    curr = node
 
    # if the current node is None and the stack is also empty, we are done
    while stack or curr:
 
        # if the current node exists, push it into the stack (defer it)
        # and move to its left child
        if curr:
            stack.append(curr)
            curr = curr.left
        
        else:
            # otherwise, if the current node is None, pop an element from the stack,
            # print it, and finally set the current node to its right child
            curr = stack.pop()
            
            if index==i:
                select[0]=index
                select[1]=curr
            index+=1
            curr = curr.right
    """ if node!=None:
            
            OS_Select(node.left,i)
            #if value!=node.key:
            index+=1
            value=node.key
            if i==index:
                select[0]=index
                select[1]=node
            
            OS_Select(node.right,i) """
            

""" 
tree=BinaryTree()
# for i in range(6):
#     num=random.randint(0,10)
#     tree.insert(num)
tree.insert(8)
tree.insert(4)
tree.insert(8)
tree.insert(6)
tree.insert(1)
tree.insert(6)
tree.insert(-4)
tree.insert(1)
tree.insert(5)
tree.insert(90)
tree.insert(54)
tree.showTreeInorder(tree.elements[0])

tree.tree_OS_Select(tree.elements[0],10)
print('OSselect tree result: '+str(select[1].key))


tree.tree_OS_Rank(tree.elements[0],8)
print('OSrank tree result: '+str(select[0])) """

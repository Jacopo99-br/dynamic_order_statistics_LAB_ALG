from enum import Enum


class Color(Enum):
    black = 0
    red = 1


class Node():
    def __init__(self,key=None,left=None,right=None,parent=None,color=None,size=None,successor=None):
        self.key=key
        self.left=left
        self.right=right
        self.parent=parent
        self.color=color
        self.size=size
        self.successor=successor

class RBtree():
    
    NIL=Node(color=Color.black,size=0)
    elements=[NIL]
    nodes=[]

    def LeftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.elements[0] = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1
    
    def RightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.elements[0] = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def insert(self, z_key):
        z=Node(z_key)
        y = self.NIL
        x = self.elements[0]
        while x != self.NIL:
            y = x
            x.size += 1
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.NIL:
            self.elements[0] = z
            self.elements[0].size = 1
        elif z.key < y.key:
            y.left = z
            z.size = 1
        else:
            y.right = z
            z.size = 1
        z.left = self.NIL
        z.right = self.NIL
        z.color = Color.red
        self.RBInsertFixup(z)
        self.findSuccessors(self.elements[0])
        self.nodes.append(z)

    def findSuccessors(self, x):
        if x != self.NIL:
            self.findSuccessors(x.left)
            self.assignSuccessor(x)
            self.findSuccessors(x.right)

    def assignSuccessor(self, z):
        z.successor = self.NIL
        if z == z.parent.left or z == self.elements[0]:
            if z.right == self.NIL:
                z.successor = z.parent
            else:
                x = z.right
                while x.left != self.NIL:
                    x = x.left
                z.successor = x
        else:
            if z.right != self.NIL:
                x = z.right
                while x.left != self.NIL:
                    x = x.left
                z.successor = x
            else:
                x = z.parent
                if x != self.NIL:
                    while x == x.parent.right:
                        x = x.parent
                        if x == self.NIL:
                            return
                    z.successor = x.parent

    def RBInsertFixup(self, z):
        while z.parent.color == Color.red:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == Color.red:
                    z.parent.color = Color.black
                    y.color = Color.black
                    z.parent.parent.color = Color.red
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.LeftRotate(z)
                    z.parent.color = Color.black
                    z.parent.parent.color = Color.red
                    self.RightRotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == Color.red:
                    z.parent.color = Color.black
                    y.color = Color.black
                    z.parent.parent.color = Color.red
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.RightRotate(z)
                    z.parent.color = Color.black
                    z.parent.parent.color = Color.red
                    self.LeftRotate(z.parent.parent)
        self.elements[0].color = Color.black

    def Min(self,start):
        while start.left.key!=None:
            start=start.left
        return start
    
    def Max(self,start):
        while start.right.key!=None:
            start=start.right
        return start

    def printTree(self,x):
        if x != self.NIL:
                return str(x.key)+'-'+str(x.color).split('.')[1]+'_'+str(x.size) + "(L: " + self.printTree(x.left) + ",R: " + self.printTree(x.right)+")"
        else:
            return "NIL"



def OS_SelectRB(x, i):
    if x == Node(color=Color.black,size=0):
        return None
    l = x.left.size + 1
    if i == l:
        #print('RB  :'+str(x.key))
        return 
    elif i < l:
        return OS_SelectRB(x.left, i)
    else:
        return OS_SelectRB(x.right, i - l)

def OS_RankRB(tree,x):
    r = x.left.size + 1
    y = x
    while y != tree.elements[0]:
        if y == y.parent.right:
            r = r + y.parent.left.size + 1
        y = y.parent
    #print('RB  :'+str(r-1))
    return 
    



""" tree=RBtree() 

tree.insert(8)
tree.insert(4)
tree.insert(8)
tree.insert(6)
tree.insert(1)
tree.insert(6)
tree.insert(-4)
tree.insert(-1)
tree.insert(5)
tree.insert(90)
tree.insert(54)

print(tree.printTree(tree.elements[0]))
print('\nOS Select RB:')
OS_SelectRB(tree.elements[0],5)
max_=tree.Max(tree.elements[0])
print('MAX:: '+str(max_.key))
print('\nOS Rank RB:')  
OS_RankRB(tree,max_)

min_=tree.Min(tree.elements[0])
print('MIN:: '+str(min_.key))
print('\nOS Rank RB:')  
OS_RankRB(tree,min_) """

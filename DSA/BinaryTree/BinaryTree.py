class Node:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class BinaryTree(Node):

    def __init__(self,data):
        self.node=Node(data)

    def insert(self,data):
        if self.node==None:
            self.node=Node(data)
        if data<self.node.data:
            self.node.left.insert(data)
        else:
            self.node.right.insert(data)





tree=BinaryTree(10)
tree.insert(8)
tree.insert(7)
tree.insert(12)
tree.insert(15)
tree.insert(2)
p=tree.insert(5)

#tree.in_order(p)
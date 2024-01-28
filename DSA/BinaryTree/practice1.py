class BinaryTree:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):

        if self.data>data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinaryTree(data)
        if self.data<data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinaryTree(data)

    def bprint(self):
        if self.left:
            self.left.bprint()
        print(self.data ,end=" ")

        if self.right:
            self.right.bprint()


def build_tree(element):
    root=BinaryTree(element[0])
    for i in element:
        root.add_child(i)
    return root
                   
if __name__ =="__main__":
    lst=[10,5,15,3,2,6,7,8]
    root =build_tree(lst)
    print(root.bprint())
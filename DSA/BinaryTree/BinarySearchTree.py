class BinaryTree:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):

        if data==self.data: #duplicate not allowed
            return
        if data <self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinaryTree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinaryTree(data)

    def inorder_print(self):
        elements=[]
      
        if self.left:
            elements +=self.left.inorder_print()
            print("left" , elements)

        elements.append(self.data)

        if self.right:
            elements +=self.right.inorder_print()
            print("Right", elements)

        return elements
    
    '''def inorder_print(self):
        if self.left:
            self.left.inorder_print()

        print(self.data , end=' ')
        
        if self.right:
            self.right.inorder_print()'''



def build_tree(element):
    root=BinaryTree(element[0])
    for i in element:
        root.add_child(i)
    return root
                   
if __name__ =="__main__":
    lst=[10,5,15,3,2,6,7,8]
    root =build_tree(lst)
    print(root.inorder_print())

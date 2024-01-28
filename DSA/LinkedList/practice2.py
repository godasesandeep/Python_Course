class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkedList:
    
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            New_node=Node(data,self.head)
            self.head=New_node

    def insert_at_end(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            itr=self.head
            while itr.next!=None:
                itr=itr.next
            itr.next=Node(data)

    def insert_at_index(self,data,index):
        if index==0:
            self.insert_at_begining(data)
        else:
            itr=self.head
            for i in range(1,index-1):
                itr=itr.next
            #itr.next=Node(data,itr.next) # It's like pointer, it is same like below code
            #or
            New_insert=Node(data,itr.next)
            itr.next=New_insert

                
    def Lprint(self):
        if self.head==None:
            print("Linked list is empty")
        itr=self.head
        while itr !=None:
            value=itr.data
            itr=itr.next
            print(value)




Llist=LinkedList()
Llist.insert_at_begining(6)
Llist.insert_at_begining(5)
Llist.insert_at_begining(4)
Llist.insert_at_begining(3)
Llist.insert_at_begining(2)
Llist.insert_at_begining(1)
Llist.insert_at_end(7)
Llist.insert_at_begining(8)
Llist.insert_at_index(10,10)
Llist.Lprint()



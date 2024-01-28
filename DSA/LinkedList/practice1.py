class Node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:

    def __init__(self):
        self.head=None

    def insert_at_start(self,data):
        new_node=Node(data,self.head)
        self.head=new_node

    def insert_at_end(self,data):
        if self.head is None:
            self.head =Node(data,None)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)

    def insert_at_index(self,data,index=0):
        if index==0:
            self.insert_at_start(data)
        else:
            itr=self.head
            for i in range(index-1):
                if itr is None:
                    print("Index out of range ....Inserted at end")
                    self.insert_at_end(data)
                    return
                itr=itr.next
               
            itr.next=Node(data,itr.next)

    def remove(self,data):
        itr=self.head
        if itr is None:
            print("There is no data present in list")
            return
        itrp=self.head
        while(itr.data !=data):
            print("I am in")
            itrp=itr
            itr=itr.next
        itrp.next=itr.next
        if itr==self.head:
            self.head=itrp.next

    def show(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr=self.head
        i=0
        string=""
        while(itr != None):
            string += str(itr.data) + ", "
            itr =itr.next
            i=i+1
            if i==50:
                return
        print(string)


llist=LinkedList()
llist.insert_at_start(1)
llist.insert_at_start(7)
llist.insert_at_start(10)
llist.insert_at_start(13)
llist.insert_at_end(11)
llist.insert_at_start(12)
llist.show()
llist.remove(12)
llist.show()
llist.insert_at_index(index=4,data=5)
llist.show()

class Node:
    def __init__(self,string=None,next=None):
        self.string=string
        self.next=next

class LinkedText:
    def __init__(self):
        self.head=None

    def add_text_at_begining(self,string):
        new_node =Node(string,self.head)
        self.head=new_node

    def add_text_at_end(self,string):
        if self.head is None:
            self.head=Node(string,None)
            return
        itr=self.head #101  Linked list node[101,105,111,126,None] -->101.next=105,105.next=111,111.next=126,126.next=None
        count=0
        while itr.next: #105,111,126,None
            count +=1   #1,2,3
            itr =itr.next #105,111,126
        print(count)
        itr.next=Node(string,None) #126.next=None=106(string,None)

    def print(self):
        if self.head is None:
            print("There is no linked test")
            return

        itr=self.head
        ltstr=""
        while itr:
            ltstr +=itr.string + " "
            itr=itr.next

        print(ltstr)


if __name__ == "__main__":

    ltx=LinkedText()
    ltx.add_text_at_begining("Ashwini")
    ltx.add_text_at_begining("You")
    ltx.add_text_at_begining("Love")
    ltx.add_text_at_begining("I")
    ltx.add_text_at_end("I L U")
    ltx.print()

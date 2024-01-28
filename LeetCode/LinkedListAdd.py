# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum1=0
        sum2=0
        add_lst=[]
        while l1 !=None and l2 !=None:
        
            sum1=sum1+l1.val +l2.val
            if sum1>=10:
                n=sum1%10
                add_lst.append(n)
                sum1=1
            else:
                add_lst.append(sum1)
                sum1=0
            #sum1=sum1*10
            l1=l1.next
            l2=l2.next
        print(add_lst)
        while l1 !=None:
            sum1=sum1+l1.val 
            if sum1>=10:
                n=sum1%10
                add_lst.append(n)
                sum1=1
            else:
                add_lst.append(sum1)
                sum1=0
            #sum1=sum1*10
            l1=l1.next
        while l2 !=None:
            sum1=sum1+l2.val 
            if sum1>=10:
                n=sum1%10
                add_lst.append(n)
                sum1=1
            else:
                add_lst.append(sum1)
                sum1=0
            #sum1=sum1*10
            l2=l2.next
        if sum1==1:
            add_lst.append(sum1)

        lst=add_lst[::-1]
        head=None
        for i in lst:

            if head is None:
                head=ListNode(i)

            else:
                new_node=ListNode(i,head)
                head=new_node
        return head



        
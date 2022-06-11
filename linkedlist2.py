from collections import defaultdict as dd

class Node:
    def __init__(self, data = None, next = None, random = None):
        self.data = data
        self.next = next
        self.random = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def printLL(self):
        if self.head is None:
            print("List is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)
    
    def insert_at_end(self,data):
        while self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def insert_values(self, dataList):
        for i in dataList:
            self.insert_at_end(i)
    
    def lengthofLL(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr=itr.next
        print(count)
    
    def remove_at_index(self, index):
        count=0
        itr = self.head
        if index == 0:
            self.head = self.head.next
            return
        while count<index-1:
            count+=1
            itr= itr.next
        itr.next = itr.next.next
    
    def insert_at_index(self,index,data):
        if index==0:
            self.insert_at_begining(data)
            return
        itr = self.head
        count = 0

        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
                break
            count+=1
            itr=itr.next
    
    def insert_after_value(self,value,data):
        itr = self.head
        while itr:
            if value==itr.data:
                itr.next=Node(data,itr.next)
                break
            itr = itr.next
    
    def remove_by_value(self,value):
        if value == self.head.data:
            self.head = self.head.next
            return

        itr=self.head
        while itr:
            if value == itr.next.data:
                itr.next = itr.next.next
                break
            itr=itr.next
            
    def findMiddle(self):
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

    
    def copyRandomList(self):
        r = h = head = self.head
        
        while h:
            node = Node(h.data)
            node.next = h.next
            h.next = node
            h = h.next.next
            
        
        while r:
            r.next.random = r.random.next if r.random else None
            r = r.next.next
            
        dummy =  Node(0)
        
        dummy.next = dc = head.next
        org = head
        front = head.next.next
        
        while org:
            org.next = front
            dc.next = front.next
            org = org.next
            front = front.next.next
        
        return dummy.next





if __name__ == "__main__":
    ll = LinkedList() #ll is declared as an object of class LinkedList

    ll.insert_at_begining(69)
    ll.insert_at_begining(79)
    ll.insert_at_begining(89)
    
    ll.insert_values([1,2,3,4])
    # ll.remove_at_index(8)
    ll.printLL()
    ll.printLL()
    # ll.findMiddle()
    ll.copyRandomList()



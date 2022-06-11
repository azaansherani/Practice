class Node:
    def __init__(self, data=None):
        self.data = data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def printLL(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr = llstr + str(itr.data) + "-->"
            itr=itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head==None:
            self.head=Node(data)
            return
        
        itr = self.head
        while itr.next:
            itr=itr.next        
        
        itr.next = Node(data)   


    def insert_dataues(self, data_list):
        for data in data_list:
            self.insert_at_end(data)


    def lengthOfLinkedList(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return(count)


    def removeAt(self, index):
        if index ==0:
            self.head=self.head.next
            return
        
        itr=self.head
        count=0
        
        while itr.next:
            itr=itr.next
            count+=1
            
            if count==index-1:
                itr.next=itr.next.next
                return
    
    
    
    
    def removeAtEnd(self):
        if self.head==None:
            print("Empty Linked List")
            return
        
        if self.head.next==None:
            self.head=None
            return

        itr = self.head
        while itr.next.next:
            itr = itr.next

        itr.next=None


    def insertAt(self, index, data):
        if index==0:
            self.insert_at_begining(data)
            return
        itr=self.head
        count=0
        while itr.next:
            itr=itr.next
            count+=1
            if count == index -1:
                node=Node(data)
                node.next = itr.next
                itr.next=node
                return

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data==data_after:
                node=Node(data_to_insert)
                node.next=itr.next
                itr.next=node
                return
            itr = itr.next


    def remove_by_value(self, data_to_be_removed):
        itr = self.head
        while itr:
            if itr.next.data==data_to_be_removed:
                itr.next=itr.next.next
                return
            itr = itr.next

    def addTwoNumbers(self, A, B):
        itr1= A
        itr2 = B

        str1=""
        while itr1:
            str1 = str1 + str(itr1.data)
            itr1=itr1.next
        str1=str1[::-1]
        str2=""
        while itr2:
            str2 = str2 + str(itr2.data)
            itr2=itr2.next
        str2=str2[::-1]
        strres = str(int(str1)+int(str2))
        strres = strres[::-1]
        print(strres)

        
        curr = A
        
        for i in strres:
            curr.data = int(i)
            curr=curr.next
        
        return A


if __name__=="__main__":
    ll1=LinkedList()
    ll2=LinkedList()
    ll1.insert_at_begining(1)
    ll1.insert_at_begining(9)
    ll1.insert_at_begining(9)
    ll2.insert_at_begining(1)
    ll1.printLL()
    ll2.printLL()

    ll3=LinkedList()
    ll3.head=ll3.addTwoNumbers(ll1.head,ll2.head)
    ll3.printLL()






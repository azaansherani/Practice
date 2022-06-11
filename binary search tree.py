class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return 
        
        if data<self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def inOrder(self):
        elements = []

        if self.left:
            elements += self.left.inOrder()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.inOrder()

        return elements

    def search(self, data):
        if self.data == data:
            return True

        if data<self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        else:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def findMin(self):
        if self.left:
            return self.left.findMin()
        return self.data

    def findMax(self):
        if self.right:
            return self.right.findMax()
        return self.data

    def preOrder(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.preOrder()
        
        if self.right:
            elements += self.right.preOrder()
        
        return elements

    def postOrder(self):
        elements = []
        if self.left:
            elements += self.left.postOrder()
        if self.right:
            elements += self.right.postOrder()
        elements.append(self.data)

        return elements

    def calculateSum(self):
        leftSum = self.left.calculateSum() if self.left else 0
        rightSum = self.right.calculateSum() if self.right else 0
        return self.data+leftSum+rightSum

    def deleteNode(self, val):
        if val< self.data:
            if self.left:
                self.left = self.left.deleteNode(val)

        elif val>self.data:
            if self.right:
                self.right = self.right.deleteNode(val)

        else: #self.data == val

            if self.left == None and self.right == None:
                return None
            elif self.left is None: #self.right ain't None
                return self.right
            elif self.right is None: #self.left ain't None
                return self.left
            
            else: #both ain't None
                min_right_tree = self.findMin()
                self.data = min_right_tree
                self.right = self.right.deleteNode(min_right_tree)
                
                # max_of_left_tree = self.left.findMax()
                # self.data = max_of_left_tree
                # self.left = self.left.deleteNode(max_of_left_tree)
        return self

            



def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.addChild(elements[i])
    return root



if __name__ == "__main__":
    elements = [17,8,2,20,9,1,18,23,18,34]
    root = buildTree(elements)

    print(root.inOrder())  
    print(root.search(20))  
    print(root.search(21))  
    print(root.findMin())
    print(root.findMax())
    print(root.preOrder())
    print(root.calculateSum())  
    print(root.inOrder())
    root.deleteNode(8)
    print(root.inOrder())
    
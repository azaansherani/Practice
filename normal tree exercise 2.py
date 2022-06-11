class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def addChild(self,child):
        child.parent = self
        self.children.append(child)

    def printTree(self,level):
        if self.getLevel()>level:
            return
        
        spaces = " " * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree(level)

    def getLevel(self):
        level = 0
        while self.parent:
            self = self.parent
            level+=1
        return level

    
if __name__ == "__main__":
    root = TreeNode("Global")
    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    gujarat.addChild(TreeNode("Ahemdabad")) 
    gujarat.addChild(TreeNode("Baroda"))
    karnataka = TreeNode("Karnanataka")
    karnataka.addChild(TreeNode("Bengaluru")) 
    mysuru = TreeNode("Mysuru")
    karnataka.addChild(mysuru) 

    india.addChild(gujarat)
    india.addChild(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.addChild(TreeNode("Princeton"))
    nj.addChild(TreeNode("Trenton"))

    california = TreeNode("California")
    california.addChild(TreeNode("San Francisco"))
    california.addChild(TreeNode("Mountain View"))
    california.addChild(TreeNode("Palo Alto"))

    usa.addChild(nj)
    usa.addChild(california)

    root.addChild(india)
    root.addChild(usa)
    mysuru.getLevel()
    root.printTree(2)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def printTree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

    def addChild(self, child):
        child.parent = self
        self.children.append(child)
        
if __name__ == "__main__":
    root = TreeNode("Electronics")
    laptops = TreeNode("Laptops")
    phones = TreeNode("Phones")
    phones.addChild(TreeNode("iPhone"))
    phones.addChild(TreeNode("Samsung")) 
    phones.addChild(TreeNode("Oneplus")) 
    laptops.addChild(TreeNode("MSI"))
    laptops.addChild(TreeNode("HP"))
    laptops.addChild(TreeNode("Dell"))
    root.addChild(laptops)
    root.addChild(phones)
    root.printTree()

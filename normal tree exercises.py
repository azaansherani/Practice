class TreeNode:
    def __init__(self, name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def printTree(self, field):
        prefix = ' ' * self.get_level() * 3
        prefix = prefix + "|__" if self.parent else ""
        if field == "both":
            print(prefix + self.name +f"({self.designation})")
        elif field == "name":
            print(prefix + self.name)
        elif field == "designation":
            print(prefix + self.designation)

        if self.children:
            for child in self.children:
                child.printTree(field)

    def addChild(self, child):
        child.parent = self
        self.children.append(child)
        
if __name__ == "__main__":

    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.addChild(TreeNode("Dhaval","Cloud Manager"))
    infra_head.addChild(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.addChild(infra_head)
    cto.addChild(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels","HR Head")

    hr_head.addChild(TreeNode("Peter","Recruitment Manager"))
    hr_head.addChild(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.addChild(cto)
    ceo.addChild(hr_head)

    ceo.printTree("name")
    print("\n")
    ceo.printTree("designation")
    print("\n")
    ceo.printTree("both")

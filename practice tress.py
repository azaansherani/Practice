class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def leftview(node,level,res):
    if node == None:
        return None
    
    if level == len(res):
        res.append(node.val)

    leftview(node.left,level+1,res)
    leftview(node.right,level+1,res)
    
def rightview(node,level,res, maxlevel):
    if node == None:
        return None
    
    if level>maxlevel[0]:
        res.append(node.val)
        maxlevel[0] = level


    rightview(node.right,level+1,res, maxlevel)
    rightview(node.left,level+1,res, maxlevel)

    


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(11)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    res = []
    leftview(root,0,res)
    res.reverse()
    maxlevel = [-1]
    rightview(root,0,res, maxlevel)
    print(res)

    # res1= []
    # rightview(root,0,res1)
    # print(res[::-1]+res1[1:])
    
"""
        1           -- 0
    2       3       -- 1
                6   -- 2

"""      

    
    

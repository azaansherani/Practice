class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isLeaf(root):
	if root.left == None and root.right == None: return True
	return False
	
def leftnodes(root, ans): #notleftview
	if not root or isLeaf(root): return
	ans.append(root.data)
	if root.left:
		leftnodes(root.left, ans)
	else:
		leftnodes(root.right, ans)

def rightnodes(root, ans):
	if not root or isLeaf(root): return
	if root.right:
		rightnodes(root.right, ans)
	else:
		rightnodes(root.left, ans)
	ans.append(root.data)

def leafnodes(root, ans):
	if root == None: return
	leafnodes(root.left, ans)
	if isLeaf(root): ans.append(root.data)
	leafnodes(root.right, ans)
	
	
def traverseBoundary(root):
	if root == None: return []
	if isLeaf(root): return [root.data]
	ans, ansr = [root.data], []
	leftnodes(root.left, ans)
	leafnodes(root, ans)
	rightnodes(root.right, ansr)
	return ans + ansr[::-1]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(11)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
print(traverseBoundary(root))
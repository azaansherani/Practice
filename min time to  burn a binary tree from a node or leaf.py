class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None



def timeToBurnTree(root, start):
	def markParents(root, parentTrack, parent=None):
		if root == None: return
		parentTrack[root] = parent
		markParents(root.left, parentTrack, root)
		markParents(root.right, parentTrack, root)
		
	parentTrack = {}
	markParents(root, parentTrack)
	
	def findStart(root):
		if root == None: return
		if root.data == start: return root
		l = findStart(root.left)
		r = findStart(root.right)
		return l or r
	
	start = findStart(root)
	visited= set()
	
	def Burn(node, distance, ans):
		if node == None or node.data in visited: return
		ans[0] = max(ans[0], distance)
		visited.add(node.data)
		for i in (node.left, node.right, parentTrack[node]):
			Burn(i, distance+1, ans)
		
	ans =[0]
	Burn(start, 0, ans)
	return ans[0]
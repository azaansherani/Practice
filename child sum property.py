def changeTree(root): 
	if root == None: return
	childSum = 0
	
	if root.left: childSum += root.left.data
	if root.right: childSum += root.right.data
	
	if childSum >= root.data: root.data = childSum
	
	else:
		if root.left: root.left.data = root.data
		if root.right: root.right.data = root.data
		
	changeTree(root.left)
	changeTree(root.right) #yahaan se root.left or right manipulate hokr aaygi so change the root value according to it
	
	total = 0
	if root.left: total += root.left.data
	if root.right: total+= root.right.data
	if root.left or root.right: root.data = total  #left and right Nodes both can be None so none of these 3 conditions will run
	
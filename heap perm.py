def heapPermutation(a, size,lstfinal):    
    if size == 1:
        lstfinal.append(a[:])
        return
    for i in range(size):
        heapPermutation(a, size-1,lstfinal)

        if size & 1:#size is odd
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]
    

nums = [2,1,3]
n = len(nums)
lstfinal=[]
heapPermutation(nums,n,lstfinal)
lstfinal.sort()
for i in range(len(lstfinal)):
    if nums == lstfinal[i]:
        nums = lstfinal[i+1]
        break
    
    if nums == lstfinal[len(lstfinal)-1]:
        nums = lstfinal[0]
        break
print(nums)



"""
heap permutation algo
"""
def heapPermutation(a, size):
 
    # if size becomes 1 then prints the obtained
    # permutation
    if size == 1:
        print(a)
        return
 
    for i in range(size):
        heapPermutation(a, size-1)
 
        # if size is odd, swap 0th i.e (first)
        # and (size-1)th i.e (last) element
        # else If size is even, swap ith
        # and (size-1)th i.e (last) element
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]
 
 
# Driver code
a = [1, 2, 3]
n = len(a)
heapPermutation(a, n)
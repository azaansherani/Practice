lst2=[]
def heapPermutation(a, size,lstfinal):    
    if size == 1:
        lstfinal.append(a[:])
        lst2.extend(a)
        return
    for i in range(size):
        heapPermutation(a, size-1,lstfinal)

        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]
    

nums = [1,2,3]
n = len(nums)
lstfinal=[]
heapPermutation(nums,n,lstfinal)
print(lstfinal,lst2)
# lstfinal.sort()
# for i in range(len(lstfinal)):
#     if nums == lstfinal[i]:
#         nums = lstfinal[i+1]
#         break
    
#     if nums == lstfinal[len(lstfinal)-1]:
#         nums = lstfinal[0]
#         break
# print(nums)

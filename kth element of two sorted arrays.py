def kthElement(arr1,arr2,n1,n2,k):
    if n2<n1: return kthElement(arr2,arr1,n2,n1,k)
    low = max(0,k-n2)
    high = min(k,n1)
    while low<=high:
        cut1 = (low+high)//2 #kitne elements ka baad cut maarna h
        cut2 = k - cut1 #second array me kitne k baad cut pdega

        l1 = float("-inf") if cut1 == 0 else arr1[cut1-1]
        l2 = float("-inf") if cut2 == 0 else arr2[cut2-1]
        r1 = float("inf") if cut1 == n1 else arr1[cut1]
        r2 = float("inf") if cut2 == n2 else arr2[cut2]
        
        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        elif l1>r2:
            high = cut1-1
        else:
            low = cut1 +1



arr1 = [100, 112, 256, 349, 770]
arr2 = [72, 86, 113, 119, 265, 445, 892]
k = 6
print(kthElement(arr1,arr2,len(arr1),len(arr2),k))


# def kthElement(arr1, arr2, k):

#     i = 0
#     j = 0
#     n1 = len(arr1)
#     n2 = len(arr2)
#     m1 = -1
#     for _ in range(k):
#         if i<n1 and j<n2:
#             if arr1[i]>arr2[j]:
#                 m1 = arr2[j]
#                 j+=1
#             else:
#                 m1 = arr1[i]
#                 i+=1
#         elif i<n1:
#             m1 = arr1[i]
#             i+=1
#         else:
#             m1 = arr2[j]
#             j+=1
            
#     return m1
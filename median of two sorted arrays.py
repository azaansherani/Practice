# def medianoftwosortedarrays(arr1,arr2,n1,n2):
#     i = 0
#     j= 0
#     m1,m2 = -1,-1
#     if (n1+n2)%2 == 1:
#         for count in range((n1+n2)//2 +1):
#             if i<n1 and j<n2:
#                 if arr1[i]>arr2[j]:
#                     m1 = arr2[j]
#                     j+=1
#                 else:
#                     m1 = arr1[i]
#                     i+=1
#             elif i<n1:
#                 m1 = arr1[i]
#                 i+=1
#             else:
#                 m1 = arr2[j]
#                 j+=1
#         return m1
#     else:
#         for count in range((n1+n2)//2 +1):
#             m2 = m1
#             if i<n1 and j<n2:
#                 if arr1[i]>arr2[j]:
#                     m1 = arr2[j]
#                     j+=1
#                 else:
#                     m1 = arr1[i]
#                     i+=1
#             elif i<n1:
#                 m1 = arr1[i]
#                 i+=1
#             else:
#                 m1 = arr2[j]
#                 j+=1

#         return (m1+m2)/2

def medianoftwosortedarrays(arr1,arr2,n1,n2):
    if n2<n1: return medianoftwosortedarrays(arr2,arr1,n2,n1)
    low = 0
    high = n1
    while low<=high:
        cut1 = (low+high)//2 #kitne elements ka baad cut maarna h
        cut2 = (n1+n2+1)//2 - cut1 #second array me kitne k baad cut pdega

        l1 = float("-inf") if cut1 == 0 else arr1[cut1-1]
        l2 = float("-inf") if cut2 == 0 else arr2[cut2-1]
        r1 = float("inf") if cut1 == n1 else arr1[cut1]
        r2 = float("inf") if cut2 == n2 else arr2[cut2]
        
        if l1<=r2 and l2<=r1:
            if (n1+n2)%2==0: return (max(l1,l2)+min(r1,r2))/2
            else: return max(l1,l2)
        
        elif l1>r2:
            high = cut1-1
        else:
            low = cut1 +1


arr1 = [1,2,5,9,10,11]
arr2 = [2,3,6,7,8]

print(medianoftwosortedarrays(arr1,arr2,len(arr1),len(arr2)))
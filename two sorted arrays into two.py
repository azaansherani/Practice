import math
def twoSortedArrays(a,b,n,m):
    print(a,b,"\n")
    gap = int(math.ceil((n+m)/2))

    while gap>0:
        i = 0
        j = gap
        while j<n+m:
            if j<n and a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
            elif j>=n and i<n and a[i]>b[j-n]:
                a[i],b[j-n]=b[j-n],a[i]
            elif i>=n and j>=n and b[i-n]>b[j-n]:
                b[i-n],b[j-n]=b[j-n],b[i-n]
            i+=1
            j+=1
        gap = 0 if gap==1 else int(math.ceil(gap/2))

    print(a,b)


# using insertion sort

# def twoSortedArrays(a,b):
#     for i in range(len(a)):
#         if a[i]>b[0]:
#             a[i],b[0] = b[0], a[i]

#         for j in range(1,len(b)):
#             key = b[j]
#             k = j-1
#             while k>=0 and key<b[k]:
#                 b[k+1] = b [k]
#                 k-=1
#             b[k+1] = key
#     print(a,b)


a = [1,4,7,8,10]
b = [2,3,9]
twoSortedArrays(a,b,len(a),len(b))
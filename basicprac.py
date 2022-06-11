def mergesort(a):
    if len(a)<=1:
        return 
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]
    mergesort(left)
    mergesort(right)

    mergetwosortedarrays(left,right,a)

def mergetwosortedarrays(a,b,arr):
    i =j =k =0
    while i<len(a) and j < len(b):
        if a[i]<=b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    arr[k:] = a[i:] if i<len(a) else b[j:]


a = [10,9,8,7,6,5,4,3,2,1,0,0,0]
mergesort(a)
print(a)

# dct = {}

# for i in range(len(a)-1,-1,-1):
#     if a[i] in dct.keys():
#         mostrecent = a[i]
        
#     else:
#         dct[a[i]]= 1

# print(dct)
# print(mostrecent)


# a = "how you doing"
# st = ""
# for i in a:
#     st = i + st
# print(st)

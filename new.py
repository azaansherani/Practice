def countElements(ele,arr):
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid]>ele:
            r = mid-1
        else:
            l = mid+1
    return l

def findMedian(a):
    low = a[0][0]
    high = 1
    n = len(a)
    m = len(a[0])

    for i in range(n):
        if a[i][0]<low:
            low = a[i][0]
        if a[i][m-1]>high:
            high = a[i][m-1]

    while low<=high:
        mid = (low+high)//2
        cnt = 0
        for i in range(n):
            cnt+= countElements(mid,a[i])

        if cnt<=(n*m)//2: low = mid+1

        else: high = mid-1

    return low

a = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]
print(findMedian(a))
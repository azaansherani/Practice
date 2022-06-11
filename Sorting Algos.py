def bubblesort(nums, k):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

        if i == k-1: #just so you can remember kth largest element
            print(nums[n-k])

    print("BubbleSort:", nums)

def mergeSort(nums, l , r):
    if l>=r: return
    
    m = (l + r)//2

    mergeSort(nums, l, m)
    mergeSort(nums, m+1, r)

    mergeTwoSortedArrays(nums, l, m, r)

def mergeTwoSortedArrays(nums, l, m, r):
    arr1 = []
    arr2 = []
    
    
    for i in range(l,m+1):
        arr1.append(nums[i])
    
    for j in range(m+1, r+1):
        arr2.append(nums[j])
    
    i = 0
    j = 0
    k = l

    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            nums[k] = arr1[i]
            i+=1

        else:
            nums[k] = arr2[j]
            j+=1
        
        k+=1
    
    while i<len(arr1):
        nums[k] = arr1[i]
        i+=1
        k+=1
    
    while j<len(arr2):
        nums[k] = arr2[j]
        j+=1
        k+=1


def insertionSort(nums):
    n = len(nums)
    for i in range(1,n):
        anchor = nums[i]
        j = i-1

        while j>=0 and nums[j]>anchor:
            nums[j+1] = nums[j]
            j-=1
        
        nums[j+1] = anchor

    print("Insertion Sort:",nums)

def selectionSort(nums):
    n = len(nums)
    for i in range(n-1):
        min_index = i

        for j in range(min_index+1, n):
            if nums[j]<nums[min_index]:
                min_index = j
        
        if i!=min_index:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    
    print("Selection Sort:", nums)

def partition(nums, l, r):
    pivot_index = l
    pivotEle = nums[l]

    while l<=r:
        while l<len(nums) and nums[l]<=pivotEle:
            l+=1
        
        while nums[r]>pivotEle:
            r-=1
        if l<r:
            nums[l], nums[r] = nums[r], nums[l]

    nums[r], nums[pivot_index] = nums[pivot_index], nums[r]

    return r
            
def quickSort(nums, start, end):
    if start<end:  # if you're sending single elements they are already at their correct pos
        pi = partition(nums, start, end)
        quickSort(nums, start, pi-1)
        quickSort(nums, pi+1, end)
    

nums = [9,2,3,4,1,5,8,10]
bubblesort(nums, 2)

nums = [9,2,3,4,1,5,8,10]
mergeSort(nums, 0, len(nums)-1)
print("MergeSort:", nums)

nums = [9,2,3,4,1,5,8,10]
insertionSort(nums)

nums = [9,2,3,4,1,5,8,10]
selectionSort(nums)

nums = [9,2,3,4,1,5,8,10]
quickSort(nums, 0, len(nums)-1)
print("QuickSort:", nums)


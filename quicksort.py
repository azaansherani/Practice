def swap(a,b,arr):
    arr[a], arr[b] = arr[b],arr[a]


def partition(arr, start, end):
    pivotindex = start
    pivotele = arr[pivotindex]
    while start<=end:

        while start<len(arr) and arr[start]<=pivotele:
            start+=1
        
        while arr[end]>pivotele:
            end-=1
            
        if start<end:
            swap(start,end,arr)

    swap(pivotindex,end,arr)
    return(end)


def quicksort(arr,start,end):
    if start<end:            
        pi=partition(arr,start,end) #partition index
        quicksort(arr,start,pi-1)
        quicksort(arr,pi+1,end)



if __name__ == "__main__":
    elements = [11,2,7,9,9,11,11,9,29,1,3,4,5,6]
    quicksort(elements,0,len(elements)-1)
    print(elements)
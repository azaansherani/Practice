def insertionSort(a):
    for i in range(1,len(a)):
        anchor = a[i]
        j = i-1
        while j>=0 and anchor < a[j]:
            a[j+1] = a[j]
            j-=1
        a[j+1] = anchor
    print(a)
    
if __name__ == "__main__":
    a = [3,9,7,1,5,6,8]
    insertionSort(a)
    


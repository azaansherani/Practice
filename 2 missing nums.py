def findTwoMissingNumbers(arr,n):
    twosum = n*(n+1)/2 - sum(arr)

    avg = twosum//2

    sumleft = 0
    sumright = 0
    for i in range(n-2):
        if arr[i]<=avg:
            sumleft+=arr[i]
        else:
            sumright +=arr[i]

    leftmissing = avg*(avg+1)/2 - sumleft

    rightmissing = twosum - leftmissing

    print(leftmissing,rightmissing)




arr = [3,4,5,6,7]
n = 2 + len(arr)
     
findTwoMissingNumbers(arr, n)
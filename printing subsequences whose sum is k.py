def subseqSumK(index, res, arr, k):
    if index == len(arr):
        if sum(res) == k:
            print(res)
        return
    
    #pick
    subseqSumK(index+1, res+[arr[index]], arr, k)

    #not pick
    subseqSumK(index+1, res, arr, k)


arr = [3,1,2,1,3]
k = 5
subseqSumK(0, [], arr, k)
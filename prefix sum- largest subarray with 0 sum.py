def maxLen( n, arr):
    dct= {}
    maxlen = 0
    sum1=0
    for i in range(n):
        sum1+=arr[i]
        if sum1 == 0:
            maxlen = max(maxlen, i+1)
        
        elif sum1 in dct:
            maxlen = max(maxlen,i - dct[sum1])
        
        else:
            dct[sum1] = i
    return maxlen
    
    #Naive Approach
    # maxl =0
    # for i in range(n-1):
    #     sum1 = arr[i]
    #     for j in range(i+1, n):
    #         sum1 += arr[j]
    #         if sum1 == 0:
    #             maxl = max(maxl,j-i+1)
                
    # return maxl

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(maxLen(len(arr), arr))

"""
largest sub array will be -2 2 -8 1 7, length: 5
"""
class Solution:
    def maxLen(self, n, arr):
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

ob = Solution()
arr= [15,-2,2,-8,1,7,10,23]
print(ob.maxLen(len(arr), arr))
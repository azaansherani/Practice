arr = [80,-50,90,100,110,-90,200]
n = len(arr)

k = 3

windowsum = sum(arr[i] for i in range(k))
maxsum = windowsum


for i in range(n-k):
    windowsum += arr[i+k] - arr[i]
    maxsum= max(maxsum,windowsum)

print(maxsum)

windowsum = 0
maxsum = 0

# l = 0
# for r in range(len(arr)):
#     if r-l+1>k:
#         windowsum -= arr[l]
#         l+=1
    
#     windowsum += arr[r]
#     maxsum= max(maxsum,windowsum)

# print(maxsum)
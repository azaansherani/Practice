""" [-2, -2, -1, -1, 0, 0, 1, 1, 1, 1, 2, 2] 
      i   j  low                          high
"""

#iterative foursum      
def fourSum(nums: list[int], target: int) -> list[list[int]]:
    n = len(nums)
    ans= []
    nums.sort()
    for i in range(n-3):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and  nums[j] == nums[j-1]:
                continue
            low = j+1
            high = n-1
            while low<high:                    
                foursum = nums[i] + nums[j] + nums[low] + nums[high]
                
                if foursum == target:
                    ans.append([nums[i], nums[j], nums[low], nums[high]])
                    
                    while low<high and nums[low] == nums[low+1]: low+=1
                    while low<high and nums[high] == nums[high-1]: high-=1
                    low+=1
                    high-=1

                elif foursum<target:
                    low+=1
                
                else:
                    high-=1
    return ans

#using the already existing three sum function
def fourSum(nums: list[int], target: int) -> list[list[int]]:
    def threesum(nums, i, ans3, target):
        for j in range(i,n-2):
            if j>i and  nums[j] == nums[j-1]:
                continue
            low = j+1
            high = n-1
            while low<high:                    
                sum3 = nums[j] + nums[low] + nums[high]
                if sum3 == target:
                    ans3.append([nums[j], nums[low], nums[high]])
                    
                    while low<high and nums[low] == nums[low+1]: low+=1
                    while low<high and nums[high] == nums[high-1]: high-=1
                    low+=1
                    high-=1
                    
                elif sum3<target:
                    low+=1
                
                else:
                    high-=1
                    
                    
    n = len(nums)
    ans= []
    nums.sort()
    for i in range(n-3):
        if i>0 and nums[i] == nums[i-1]:
            continue
        ans3 = []
        threesum(nums, i+1, ans3, target-nums[i])
        for k in ans3:
            ans.append([nums[i]]+k)
        
    return ans

#BEST SOLUTION TAKEN FROM LEETCODE
def fourSum(self, nums, target):
    def findNsum(nums, target, N, result, results):
        if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            l,r = 0,len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l<r and nums[r]==nums[r-1]: r-=1

                    l+=1
                    r-=1

                elif s < target:
                    l += 1

                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

    results = []
    findNsum(sorted(nums), target, 4, [], results)
    return results





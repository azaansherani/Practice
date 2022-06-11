""" Time Complexity: O(n^2) ; Space: O(m) but that's the required answer so Auxiliary space complexity is O(1) """

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    ans = []
    
    for i in range(len(nums)-2):            #b + c = -a,     a is nums[i]
        
        if i>0 and nums[i]==nums[i-1]: #duplicate i are ignored
            continue
            
        low = i+1
        high = len(nums)-1
        
        while low<high:
            sumOT = nums[low]+nums[high]    #sum of other two
            
            if sumOT == -nums[i]:
                ans.append([nums[low], nums[i], nums[high]])
                
                #all the similar lows are ignored for the next step
                while low<high and nums[low]==nums[low+1]: 
                    low+=1
                    
                    
                while high>low and nums[high] == nums[high-1]:
                    high-=1
                    
                low+=1
                high-=1
                
            elif sumOT<-nums[i]:
                low+=1
                
            else:
                high-=1
    return ans

print(threeSum([-1,0,1,2,-1,-4]))



"""Time: O(n^2) triplets ki sorting itna nhi legi, or bhi kuch kuch h like check kr rhe if list in ans, sort kr rhe,
This code is not working in LeetCode, better not mention this anywhere, striver said TC to be (O(n^2) * log(m)), log m usne set use kra h uske insertion ka h;
Space: O(m) + O(n); O(m) for dict """

def threeSum(nums: list[int]) -> list[list[int]]: 
    n = len(nums)
    dct = {}
    ans = []
    for i in nums:
        if i in dct:
            dct[i]+=1
        else:
            dct[i] = 1
    print(dct)
    
    for i in range(n-1):
        dct[nums[i]] -= 1 
        for j in range(i+1,n):
                dct[nums[j]] -=1
                diff = -nums[i] - nums[j]
                if diff in dct and dct[diff]!=0:
                    lst = [diff,nums[i],nums[j]]
                    lst.sort()
                    if lst not in ans:
                        ans.append(lst)
                dct[nums[j]] +=1
        dct[nums[i]] += 1
    return ans

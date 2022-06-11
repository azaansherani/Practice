#Backtracking Questions

def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(index, nums, temp, ans, N):
            ans.append(temp)
            for i in range(index,N):
                dfs(i+1, nums, temp+[nums[i]], ans, N)
        ans = []
        dfs(0, nums, [], ans, len(nums))
        return ans

"-----------------------------------------------------------------------------------------------------------"

def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
    def dfs(index, nums, temp, ans, N):
        ans.append(temp)
        for i in range(index, N):
            if i!=index and nums[i] == nums[i-1]: continue
            dfs(i+1, nums, temp+[nums[i]], ans, N)

    ans = []
    nums.sort()
    dfs(0, nums, [], ans, len(nums))
    return ans

"-----------------------------------------------------------------------------------------------------------"

def permutations(self, nums: list[int]) -> list[list[int]]:
    def helper(nums, temp, ans):
        if not nums:
            ans.append(temp)

        for i in range(len(nums)):
            helper(nums[:i] + nums[i+1:], temp+[nums[i]], ans)

    ans = []
    helper(nums, [], ans)
    return ans

"-----------------------------------------------------------------------------------------------------------"

def permutations2(self, nums: list[int]) -> list[list[int]]:
    def helper(nums, temp, ans):
        if not nums:
            ans.append(temp)

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: continue
            helper(nums[:i] + nums[i+1:], temp+[nums[i]], ans)

    ans = []
    nums.sort()
    helper(nums, [], ans)
    return ans

"-----------------------------------------------------------------------------------------------------------"

def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
    def dfs(index, nums, temp, ans, target, N):
        if target<=0:
            if target == 0:
                ans.append(temp)
            return
        
        for i in range(index, N):
            dfs(i, nums, temp+[nums[i]], ans, target-nums[i], N)
    
    ans = []
    dfs(0 , candidates, [], ans, target, len(candidates))
    return ans
        
"-----------------------------------------------------------------------------------------------------------"

def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
    n = len(candidates)
    def dfs(index, temp, nums, ans, target):
        if target<=0:
            if target == 0:
                ans.append(temp)
            return
                
        for i in range(index, n):
            if i!=index and nums[i] == nums[i-1]: continue
            dfs(i+1, temp+[nums[i]], nums, ans, target - nums[i])
    
    ans = []
    candidates.sort()
    dfs(0, [], candidates, ans, target)
    return ans        

"-----------------------------------------------------------------------------------------------------------"

def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []
        
        dct = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        def backtracking(i, s = ""):
            if i == len(digits):
                res.append(s)
                return
            for char in dct[digits[i]]:
                backtracking(i+1, s + char)
        
        backtracking(0)
        return res

"-----------------------------------------------------------------------------------------------------------"

def combinationSum3(self, k: int, n: int) -> list[list[int]]:
    ans = []
    def backtracking(i, sum1 =0, count = 0, res = []):
        if i>10: return

        if sum1 == n and count == k:
            ans.append(res)
            return
        
        backtracking(i+1, sum1 + i, count+1, res + [i])
        backtracking(i+1, sum1, count, res)
        
    backtracking(1)
    return ans
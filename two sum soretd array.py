"""In this case they asked us to return index+1 therefore there's a plus one"""

# Two Pointers O(n), O(1)
def twoSum(numbers: list[int], target: int) -> list[int]:
    # if array is not sorted sort it, just for an approach
    l = 0
    r = len(numbers)-1
    while l<r:
        s = numbers[l] + numbers[r]
        if s == target:
            return l+1,r+1
        
        elif s<target:
            l+=1
        else:
            r-=1
            
        
#hashing approach O(n), O(n)
def twoSum(numbers: list[int], target: int)]:
    dct = {}
    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in dct:
            return (dct[diff]+1, i+1)
        dct[numbers[i]] = i

#Binary Search Approach O(nlog(n)) , O(1)
def twoSum(self, numbers: list[int], target: int) -> list[int]:
    for i in range(len(numbers)):
        l = i+1
        r = len(numbers)-1
        diff = target - numbers[i]
        while l<=r:
            mid = l +(r-l)//2
            if numbers[mid] == diff:
                return i+1,mid+1
            elif numbers[mid]<diff:
                l = mid+1
            else:
                r = mid-1
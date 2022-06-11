def np(nums):
    index=0
    flag=True
    for i in range(len(nums)-1,0,-1):
        if nums[i]>nums[i-1]:
            index = i-1
            flag=False
            break
    if flag:
        return nums[::-1]
    for i in range(len(nums)-1,index,-1):
        if nums[i]>nums[index]:
            nums[i],nums[index]=nums[index],nums[i]
            break
    
    return nums[:index+1]+nums[len(nums):index:-1]
nums=[1,3,2]
print(np(nums))
            
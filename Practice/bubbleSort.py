nums = [2,0,2,1,1,0]

for j in range(len(nums)):
    for i in range(len(nums) -1):
        if nums[i] > nums[i+1]:
            nums[i],nums[i+1] = nums[i+1],nums[i]

print(nums)

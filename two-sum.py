def twoSum(nums, target):
        for i in range(len(nums)):
            for b in range(i+1, len(nums)):
                if((nums[i]+nums[b]) == target):
                    return [i, b]
nums = [2,4,5,6,8]
target = 9
print(twoSum(nums, target))
#LeetCode: 1. Two Sum Problem
# Problem Link: https://leetcode.com/problems/two-sum/description/
def twoSum(nums, target):
        for i in range(len(nums)):
            for b in range(i+1, len(nums)):
                if((target-nums[i]) == nums[b]):
                # Another Approach which is more easy to understand is:
                # if((nums[i]+nums[b])==target):
                    return [i, b]
nums = [2,4,5,6,8] # You can adjust it
target = 9 # You should write something which your two values from nums can add to become
print(twoSum(nums, target))
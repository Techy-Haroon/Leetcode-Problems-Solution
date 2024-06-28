#LeetCode: 217. Contains Duplicate
# Problem Link: https://leetcode.com/problems/contains-duplicate/description/
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
nums = [1,3,2,1]
print(containsDuplicate(nums)) # If array nums contain duplicate number, we will have True. Otherwise False.
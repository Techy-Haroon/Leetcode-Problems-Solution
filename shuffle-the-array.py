# LeetCode: 1470. Shuffle the Array
# Problem Link: https://leetcode.com/problems/shuffle-the-array/description/
def shuffle(nums, n):
    matches = []
    for i in range(n):
        matches.append(nums[i])
        matches.append(nums[i+n])
    return matches
nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))
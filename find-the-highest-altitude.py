# LeetCode: 1732. Find the Highest Altitude
# Problem Link: https://leetcode.com/problems/find-the-highest-altitude/description/
def largestAltitude(gain):
    current = 0
    highest = 0
    for i in gain:
        current += i
        highest = max(highest, current)
    return highest
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))
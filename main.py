import sys
import os
import time
def list_verify(nums):
    try:
        nums = nums.split(',')
        for index,i in enumerate(nums, start=0):
            try:
                nums[index] = int(nums[index])
            except:
                clear()
                print("Sorry, You didn't enter a Valid List Number")
                main()
        return nums
    except Exception as e:
        clear()
        print("Sorry, an error occured.", e)
        main()
def number_verify(number):
    try:
        target = int(number)
        return target
    except:
        clear()
        print("Valid target wasn't added.")
        main()
def clear():
    os.system("cls")
#LeetCode: 1. Two Sum Problem
# Problem Link: https://leetcode.com/problems/two-sum/description/
def twoSum(nums, target):
        for i in range(len(nums)):
            for b in range(i+1, len(nums)):
                if((nums[i]+nums[b]) == target):
                    return [i, b]
#LeetCode: 217. Contains Duplicate
# Problem Link: https://leetcode.com/problems/contains-duplicate/description/
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
# LeetCode: 1732. Find the Highest Altitude
# Problem Link: https://leetcode.com/problems/find-the-highest-altitude/description/
def largestAltitude(gain):
    if len(gain) <= 1:
        return gain[0]
    current = 0
    highest = 0
    for i in gain:
        current += i
        highest = max(highest, current)
    return highest
# LeetCode: 1512. Number of Good Pairs
# Problem Link: https://leetcode.com/problems/number-of-good-pairs/description/
def numIdenticalPairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count
# LeetCode: 1470. Shuffle the Array
# Problem Link: https://leetcode.com/problems/shuffle-the-array/description/
def shuffle(nums, n):
    matches = []
    for i in range(n):
        matches.append(nums[i])
        matches.append(nums[i+n])
    return matches

def main():
    print("Please Choose the Problem:\n1. Two Sum\n2. Contains Duplicate\n3. Find the Highest Altitude\n4. Find the Good Pairs\n5. Shuffle the Array\n6. Exit")
    user_input = "0"
    user_input = input("")
    if not user_input:
        clear()
        print("Please enter a valid approach")
        main()
    elif(user_input=="1"):
        while True:
            nums = input("Enter numbers in this form:\n1,2,3,4...\n")
            nums = list_verify(nums)
            target = input("Please enter a target number:\n")
            target = number_verify(target)
            break
        output = twoSum(nums, target)
        if not output:
            clear()
            print("Sorry, There was problem with your inputs. Maybe no combination can combine to target number.")
        else:
            clear()
            num1, num2 = output
            print(f"Your Output is: {output} as the real values are:\n{[nums[num1], nums[num2]]}\nand sum of {nums[num1]} + {nums[num2]} = {target} (target number)")
        main()
    elif(user_input=="2"):
            nums = input("Enter numbers in this form:\n1,2,3,4...\n")
            nums = list_verify(nums)
            output = containsDuplicate(nums)
            if output == True:
                clear()
                print(f"A Duplicate was found. Output = {output}")
            else:
                clear()
                print(f"A Duplicate was not found. Output = {output}")
            main()
    elif(user_input=="3"):
        gain = input("Enter the gain in the following form to find highest altitude:\n1,2,3,4...\n")
        gain = list_verify(gain)
        output = largestAltitude(gain)
        clear()
        print(f"Highest Altitude with this gain list: {gain} is {output}")
        main()
    elif(user_input=="4"):
        nums = input("Please enter numbers in the following form to find good paris:\n1,2,3,4...\n")
        nums = list_verify(nums)
        output = numIdenticalPairs(nums)
        clear()
        print(f"For this list: {nums}, there are total {output} good pairs.")
        main()
    elif(user_input=="5"):
        nums = input("Enter numbers in the following form to shuffle it:\n1,2,3,4...\n")
        nums = list_verify(nums)
        n = input("Please enter value of n:\n")
        n = number_verify(n)
        if(n != (len(nums)/2)):
            clear()
            print("Value of n must be half of length of array.")
            main()
        output = shuffle(nums, n)
        clear()
        print(f"Given array was {nums} and shuffled form of array with given value of n: {n} is:\n{output}")
        main()
    elif(user_input=="6"):
        for i in range(3, -1, -1):
            clear()
            print(f"Exiting Program in {i} seconds...")
            time.sleep(1)
        print("Exited...")
        sys.exit()
    else:
        clear()
        print("No valid choice was made. Try again")
        main()
main()
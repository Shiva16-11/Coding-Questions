# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
#  such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets. 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

def checkTwoSum(nums, target, index):
    global ans
    start = index + 1
    n = len(nums)
    end = n - 1
    flag = 0
    while start <= end:
        if nums[start] + nums[end] == target:
            flag = 1
            if (start != end):
                ans.add((nums[index], nums[start], nums[end]))
            start += 1
        elif nums[start] + nums[end] < target:
            start += 1
        else:
            end -= 1  
    



def solve(nums):
    n = len(nums)
    ans = set()
    ref = set()
    out = []
    nums = sorted(nums)
    for i in range(n):
        if nums[i] not in ref:
            ref.add(nums[i])
            checkTwoSum(nums, -1 * nums[i], i)
    for x in ans:
        out.append(list(x))        
    print(out)

# driver code
solve(nums)


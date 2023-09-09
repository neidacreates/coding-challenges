'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# SOLUTION EXPLANATION
# create a dictionary to store the number and it's index
# loop through the list and subtract the target from the current number
# check if the answer is in the dictionary already, this means the match for the sum has already been encountered
# if it is in the dict already, return the index of the match and the current index
# if it is not in the dictionary already, add it (the number and its index)
# since there is for sure one answer, there is no need to have a return [] clause for cases where there is no answer
# time complexity O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i in range(len(nums)):
            answer = target - nums[i]
            if answer in hash_map:
                return [hash_map[answer], i]
            else:
                hash_map[nums[i]] = i

# SAMPLE SOLUTION
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


# attempted solution with 2 pointers?
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         slow_pointer = [0, nums[0]]
#         fast_pointer = [1, nums[1]]

#         while slow_pointer:
#             if slow_pointer[1] + fast_pointer[1] == target:
#                 return [slow_pointer[0], fast_pointer[0]]
#             fast_pointer[0] += 1
#             fast_pointer[1] = nums[fast_pointer[0]]
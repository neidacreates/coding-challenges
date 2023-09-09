# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return not (len(nums) == len(set(nums)))
    
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        frequencies = {}
        for element in nums:
            if element in frequencies:
                frequencies[element] += 1
            else:
                frequencies[element] = 1
        for frequency in frequencies.values():
            if frequency > 1:
                return True
        return False

# sample solutions

class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            else:
                num_set.add(i)
        return False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

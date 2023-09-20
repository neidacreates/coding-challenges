'''
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make a set out of the list of nums to ge rid of duplicates
        num_set = set(nums)
        # initialize the longest length to 0 
        longest = 0
        # iterate through nums set and see if the current number is the start of a sequence by checking if a number that's 1 less than it is not present 
        for number in num_set:
            if (number - 1) not in num_set:
                # initialize the length of the sequence as 1 if the number is the start of a sequence
                length = 1
                # while the following numbers in the sequence are present in the set, keep increasing the length of the sequence
                while (number + length) in num_set:
                    length += 1
            # redefine longest to be the maximum between the length of the current sequence or the longest length currently stored
                longest = max(length, longest)
        return longest
    
# SAMPLE SOLUTION
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

'''
# SOLUTION WALKTHROUGH
# put the array in ascending order (sort) 
# then iterate through the array
# if the first number is positive, that means there will be no answer (starting from 2, for example, and then getting to 0 without any negatives summed to it is impossible)
# if the current value is the same as the one before it (this is a duplicate) then skip it
# make two pointers, one from the left (value after the current value) and one from the right (end of list)
# solve like two sum II aka shift pointers depending on the sum compared to target (in this case 0)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for index, current_number in enumerate(nums):
            # skip the positive numbers
            if current_number > 0: 
                break
            # skip the duplicates
            if index > 0 and current_number == nums[index-1]:
                continue
            # make left and right pointers
            left, right = index + 1, len(nums) - 1
            # while the left pointer is less than the right
            while left < right:
                total_sum = current_number + nums[left] + nums[right]
                if total_sum > 0:
                    right -= 1
                elif total_sum < 0:
                    left += 1
                # else the sum is 0 so add it to the answer
                else:
                    answer.append([current_number, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # if the next number on the left pointers path is a duplicate, keep adding 1 to left to move on
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return answer
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # First: find the prefix products and save them to the answer array
        # Second: find the postfix products and multiply them by the prefixes saved in answer, saving final value in answer

        # initialize an answer array that's the same length as the input array but with placeholders
        answer = [1] * (len(nums))
        # loop through input array from index 1 to the right (start at 1 because there is no prefix product before index 0)
        # on first pass set the first answer index to the first number in nums (answer[1] = answer[0] (which is 1) * nums[0])
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
        postfix = 1
        # loop through nums again but backwards, from the second to last item, multiply answer at each index by the postfix, then update postfix by multiplying by the  and calculate postfix, then multiply it by the prefix value in answer and save overall result to answer array
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer

# SAMPLE SOLUTIONS
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length
        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(length-2, -1, -1):
            products[i] *= right
            right *= nums[i]
        
        return products

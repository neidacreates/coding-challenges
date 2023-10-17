'''
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104

'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # height of smaller line x difference between the indexes of both lines
        # for example 1 -> 7 (height of line) x (8-1 = 7) (difference between line indexes)) = 49

        # two pointers
        # left starts out at the left (0 index) and right starts at the last index
        # calculate water size and compare to greatest value currently stored
        # if its greater replace this value in memory
        #move the pointer that is on the lesser sized line over by one
        #calculate again and compare
        result = 0
        left = 0 
        right = len(height) - 1
        while left < right:
            difference = right - left
            smallest = min(height[left], height[right])
            water = smallest * difference
            if water >= result:
                result = water
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result
    
# SAMPLE SOLUTION
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
        return res

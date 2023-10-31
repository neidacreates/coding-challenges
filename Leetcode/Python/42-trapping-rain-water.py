'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
'''
# APPROACH 
# two pointers
# left pointer set to 0 and right set to the last element in the list
# set up variables to track the largest left value and right value (set them to the value of the pointers)
# variable to store the result set to 0
# iterate through the list, while the left pointer is less than the right
# move the pointer corresponding to the lesser of the maxleft or maxright values
# for example, if the left max is less than the right max, move the left pointer
# after moving the pointer, update the maxleft or maxright if the current position in the list (where the pointer is) is greater
# add the difference between the corresponding max value and the current value to the result

# SAMPLE SOLUTION
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

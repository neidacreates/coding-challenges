'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

'''
def search(nums, target):
    # binary search approach
    # find the middle index of the nums list 
    # compare the item at this middle index with the target
    # if it is the target then return index
    # otherwise if this num is > target, reduce search window to the numbers below this current number
    # otherwise if the num < target, search in the window of nums that is above this current index

    high = len(nums)-1
    low = 0 

    while low <= high:
        middle = (high+low) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            high = middle-1
        else:
            low = middle+1
    return -1



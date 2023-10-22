'''
Given a string s, find the length of the longest
substring
without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

'''
# APPROACH
# make a set to store all the letters
# make right and left pointers for the sliding window
# iterate through the list and check if the right pointer is a character that is already in the set, if it is,
# shorten the window by removing the leftmost letter (where the left pointer is)
# and move the left pointer over 
# if the right pointer is not in the set, then add it
# reset the result to the max of the current result or the size of the current window

# SAMPLE SOLUTION
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        result = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[r])
            result = max(result, r - left + 1)
        return result
    
# https://youtu.be/pY2dYa1m2VM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length

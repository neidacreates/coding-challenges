'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        
        for letter in t:
            if pointer < len(s):
                if letter == s[pointer]:
                    pointer += 1
        if pointer == len(s):
            return True
        return False
                

# SAMPLE SOLUTION 
# make two pointers to keep track of index in both strings
# while the s pointer is less than its length and the t pointer is less than length of t
# compare the current letters at each pointer
# if they are the same letter, move the s pointer over to the next letter 
# regardless if the were the same letter or not, move the t pointer over
# if all of the letters in s are in t, the s pointer will increase to the length of s
# thus, return whether the s pointer is equal to the length of s, true means it is a subsequence and false means its not
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

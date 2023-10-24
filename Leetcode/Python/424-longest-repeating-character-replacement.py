'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.


Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

'''
# left pointer at 0
# right pointer goes through every position until the end of the string
# for character at position r, increment its count in the dictionary (1 + whatever it currently was/or 0 if it was empty)
# length of the current window is r - left + 1
# if the window is not valid (if the size of the window minus the size of the greatest character is greater than the # of switches we have (k) / if the number of non-greatest character exceeds the number of switches)
# then move the left pointer over and decrease the count of the left pointer letter in the dictionary, since it's no longer in the window
# result is set to the max of result or the size of the current window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, r - left + 1)
        return result
    
# SAMPLE SOLUTION
# https://www.youtube.com/watch?v=gqXU1UyA8pk
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)

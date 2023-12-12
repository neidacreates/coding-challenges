'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.

'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # input = string with spaces and letters
        # output = integer reppresenting the length of the last word in the string (word is something without spaces)
        
        # looping through the string from the right (the end)
        # have a variable (count) to store the length
        # when looping, if the current character is a space, keep going
        # if the character is not a space, count +1 
        # keep going until you hit a space
        # break out of the loop 

        count = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and count == 0:
                continue
            elif s[i] != " ":
                count += 1
            else:
                break

        return count
    
# EXAMPLE SOLUTION NEETCODE
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
	one shortcut
	"""
	#	return len(s.split()[-1])
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c

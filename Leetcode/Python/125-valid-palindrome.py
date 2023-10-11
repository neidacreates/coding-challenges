'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove the non-alpha characters first
        # two pointers: one from the right and one from the left
        # compare letters at each pointer, if they differ return false, else keep going
        # keep going until you reach the middle (length // 2)

        # return true
        new_string = ""

        for character in s:
            if character.lower() in "abcdefghijklmnopqrstuvwxyz0123456789":
                new_string += character.lower()
        print(new_string)
        i = 0
        j = len(new_string)-1

        while i < (len(new_string)//2):
            if new_string[i] != new_string[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    
# SAMPLE SOLUTION
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

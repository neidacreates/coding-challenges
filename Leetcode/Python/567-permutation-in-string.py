'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.

'''
# APPROACH
# sliding window
# make a window that is the length of the s1 and move it over by one letter
# start at the index 0 through (len(s1) -1)
# check if that substring of s2 has the letters from s1
# return true if so
# iterate all the way to the end of s2 then return false if no permutation was found

# INCOMPLETE SOLUTION - PASSING 100/108 TEST CASES
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = Counter(s1)
    
        left = 0
        right = len(s1)

        while right <= len(s2):
            for letter in s2[left:right]:
                if letter in s1_dict and s1_dict[letter] != 0:
                    s1_dict[letter] -= 1
            if sum(s1_dict.values()) == 0 and -1 not in s1_dict.values():
                return True
            else:
                left += 1
                right += 1
                if s2[left-1] in s1_dict:
                    s1_dict[s2[left-1]] += 1
        return False


# SAMPLE SOLUTIONS
def checkInclusion(self, s1: str, s2: str) -> bool:
	cntr, w = Counter(s1), len(s1)   

	for i in range(len(s2)):
		if s2[i] in cntr: 
			cntr[s2[i]] -= 1
		if i >= w and s2[i-w] in cntr: 
			cntr[s2[i-w]] += 1

		if all([cntr[i] == 0 for i in cntr]): 
			return True

	return False

# ===========================================
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

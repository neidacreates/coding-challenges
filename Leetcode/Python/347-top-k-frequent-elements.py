'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

'''
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # frequencies dictionary example
        # {
        #     1: 3,
        #     2: 2,
        #     3: 1
        # }

        
        frequencies = defaultdict(int)
        answer = []
        # loop through nums and make an entry in the dictionary for each integer, the value will be the frequency it shows up in the nums list
        for element in nums:
                frequencies[element] += 1
        # loop through the dictionary and push the key value pairs into the answer heap until we reach an answer length of k. After that, replace the key value pairs in the answer only if there are other values that are greater than the ones already there.
        for key, val in frequencies.items():
            if len(answer) < k:
                heapq.heappush(answer, [val,key])
            else:
                heapq.heappushpop(answer, [val,key])
        # return the key (the integer) not the value (the frequency)
        return [y for x,y in answer]
    
"""
SAMPLE SOLUTIONS
"""
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n) bucket sort

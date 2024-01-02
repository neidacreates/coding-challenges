'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23


Constraints:

    1 <= piles.length <= 104
    piles.length <= h <= 109
    1 <= piles[i] <= 109


'''
# EXPLANATION   
# binary search
# you're trying to find the minimum value within 1 through maximum pile that could be k
# for example, if you have Input: piles = [3,6,7,11], h = 8; then you would look within [1,2,3,4,5,6,7,8,9,10,11] for the smallest k that would let Koko eat all the bananas

# APPROACH
# set left pointer to 1 and right pointer to max(piles)
# while the left is less than or equal to the right,
# calculate k which is the middle value between the left and right
# set an hours placeholder to 0
# iterate through the piles and calcualte how many hours it would take to eat that pile (pile / k)
# add the hours to the hours placeholder
# after going through all the piles, you have a total of how many hours it would take to eat them with the current k
# if the total hours are less than or equal to h, the result is k and you then check the values that are smaller than k (move right pointer to k - 1)
# if the hours are greater than h, check the values above the current k - move the left pointer to k + 1

# TIME COMPLEXITY 
# O(log(max(piles)*piles)) -> O(nlog(n))
# SPACE COMPLEXITY
# O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # input = piles array, h integer
        # output = k integer
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result
    

# OTHER SOLUTION
# finds the bounds of k first, and then does binary search within those
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        hours_taken = sum(piles)
        while hours_taken > h:
            k *= 2
            hours_taken = sum([math.ceil(p / k) for p in piles])
        if k == 1:
            return k

        l = k/2
        while l < k:
            mid = (l + k) // 2
            val = sum([math.ceil(p / mid) for p in piles])

            if val <= h:
                k = mid
            else:
                l = mid + 1
        return int(k)

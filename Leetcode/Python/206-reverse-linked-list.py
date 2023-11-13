'''
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []


Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# APPROACH 
# iterative solution:
# two pointers
# previous set to null, current set to head
# current.next points to previous pointer; then shift each pointer over
# when you reach the end of list, previous.next points to null which is current
# the new head is previous pointer, that's what you return

# ==========================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative
        # T O(n)
        # M O(1)
        previous, current = None, head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive
        # T O(n)
        # M O(n)
        # base case
        if not head:
            return None
        newHead = head
        # if there's still a subproblem left
        if head.next:
            newHead = self.reverseList(head.next)
            # reversing the link between the next node and head
            head.next.next = head
        head.next = None
        return newHead
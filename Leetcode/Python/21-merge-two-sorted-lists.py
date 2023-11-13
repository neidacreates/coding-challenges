'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

'''
# ITERATIVE APPROACH
# make a dummy node to be the head of the new list
# iterate through both lists while they are not empty (two pointers)
# compare the current nodes and add the smaller one to the new list (current_new_list_node.next)
# move over the pointer corresponding to the list of the node just added
# move the new list current node over
# afterwards, if one list is longer than the other, add it to the new list as a whole since its already sorted
# return the dummy.next because that's the head of the new list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




# SAMPLE SOLUTION
# iterative
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
    
# recursive
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # base case (if one list node is empty, return the next one)
        if not list1:
            return list2
        if not list2:
            return list1
        # compare both nodes and assign small and big accordingly
        if list1.val < list2.val:
            small = list1
            big = list2
        else:
            small = list2
            big = list1
        # recursively do the same on a smaller subsection of the list with the smaller item
        small.next = self.mergeTwoLists(small.next, big)
        return small
        

        
'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false


The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are empty
        if not p and not q:
            return True
        # if both are not empty and the current node values are equal
        if p and q and p.val == q.val:
            # recursively call the function on the left and right subtrees of each tree. using "and" to return "true and true" or "true and false"
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # if one tree is empty and the other isnt, or if both are not empty but the current nodes arent equal to each other, return false meaning they are not equal trees overall
        else:
            return False
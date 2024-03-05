'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # make a helper function to compare two trees to see if they are the same
    def isSame(self, root, subRoot):
        # if both trees are empty, they are the same so return True
        if not root and not subRoot:
            return True
        # if both trees are not empty and the values of the current root nodes are the same, recursively check the left subtrees and right subtrees of both to make sure they are also the same
        if root and subRoot and root.val == subRoot.val:
            return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)
        # if none of the conditions are met, return false as the trees must not be equal
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if the main tree is populated and the sub tree is empty, its true because an empty subtree can be one of the leafs in the main tree
        if root and not subRoot: 
            return True
        # if the main tree is empty return false because a populated subtree cant be in an empty tree
        if not root:
            return False
        # call the helper function to see if both trees are the same, if they are then return true
        if self.isSame(root, subRoot):
            return True
        # if the call to the helper did not return true, then check if the subRoot subtree is a subtree of the main tree's subtrees (so check both left and right subtrees of the main one). We use "or" because the subtree just has to exist once, on either side. 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

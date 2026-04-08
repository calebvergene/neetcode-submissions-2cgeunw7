# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ## thought process. give a func root.left and root.right then 
        ## find the max depths of those. then compare. 
        if not root:
            return True
        balanced = True
        def findLength(node, depth):
            #base case
            if not node:
                return depth
            depth += 1
            dleft = findLength(node.left, depth)
            dright = findLength(node.right, depth)
            nonlocal balanced
            balanced = balanced and abs(dleft - dright) < 2
            return max(dleft, dright)
        findLength(root, 0)
        return balanced
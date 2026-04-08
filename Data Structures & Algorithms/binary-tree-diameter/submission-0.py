# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def longest_path(node):
            if not node:
                return 0 
            left_side = longest_path(node.left)
            right_side = longest_path(node.right)

            nonlocal longest 
            print(node.val, left_side, right_side)
            longest = max(longest, left_side+right_side)

            return max(left_side + 1, right_side + 1)
        longest_path(root)
        return longest 
        
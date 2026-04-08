# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        small = None
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            nonlocal k
            k-=1
            if k == 0:
                nonlocal small
                small = node
            dfs(node.right)
        dfs(root)
        return small.val
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 
        value = -1
        
        def dfs(node):
            nonlocal count, value
            if not node or value != -1:
                return 
            
            dfs(node.left)
            count += 1
            if count == k:
                value = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return value
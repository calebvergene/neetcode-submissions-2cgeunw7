# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ## so if you come across a negative number and it 
        ## makes the total path below 0, then reset path to 0
        max_path = float('-inf')
        def dfs(node):
            nonlocal max_path
            if not node:
                return 0
            # checking current node
            left = dfs(node.left)
            right = dfs(node.right)
            max_path = max(right + left + node.val, max_path)
            
            # choose what to return for right/left
            max_side = max(left, right)
            if max_side + node.val < 0:
                return 0 
            return max_side + node.val
        dfs(root)
        return max_path
        
            
                
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nd = None
        def dfs(node):
            nonlocal nd
            if not node: 
                return False, False
            
            x, y = dfs(node.left)
            z, a = dfs(node.right)

            c = z or x or node == p
            b = y or a or node == q
            if c and b:
                nd = node
                return False, False
            else:
                return c, b
        dfs(root)
        return nd
                



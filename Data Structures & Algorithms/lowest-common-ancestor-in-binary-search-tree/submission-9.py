# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None

        def dfs(root):
            if not root:
                return False, False
            l = dfs(root.left)
            r = dfs(root.right)

            p_found = l[0] or r[0] or root.val == p.val
            q_found = l[1] or r[1] or root.val == q.val

            nonlocal res
            if p_found and q_found and res == None:
                res = root
            
            return p_found, q_found
        
        dfs(root)
        return res
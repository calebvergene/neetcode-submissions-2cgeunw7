# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        def dfs(node, max_node):
            if not node:
                return
            if node.val >= max_node:
                nonlocal total 
                total += 1
                max_node = node.val
            dfs(node.left, max_node)
            dfs(node.right, max_node)


        dfs(root, float('-inf'))
        return total
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # use dfs.
        # at each node, either count (parent + past children) or (both children), 
        # basically just see if below is bigger or below below is bigger
        def dfs(node):
            if not node:
                return 0, 0, 0

            # child, grandchild, ggc
            left_child, left_grand_child, lggc = dfs(node.left)
            right_child, right_grand_child, rggc = dfs(node.right)
            children = max(left_child, left_grand_child) + max(right_child, right_grand_child)
            grand_children = left_grand_child + right_grand_child
            great_grand_children = lggc + rggc

            max_val = node.val + max(grand_children, great_grand_children)
            return max_val, children, grand_children

        return max(dfs(root))

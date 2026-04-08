# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            # this is for if its a deadend on one side
            if not node:
                return (None, False) # node, deleted
            # is a leaf node and is target: then delete the node
            if not node.left and not node.right and node.val == target:
                return (None, True)
            
            node.right, deletedr = dfs(node.right)
            node.left, deletedl = dfs(node.left)

            deleted = deletedr or deletedl
            # prevents infinite loop. if child deleted, then need to recheck 
            if deleted:
                return dfs(node)
            else:
                return (node, False)
        return dfs(root)[0]
            
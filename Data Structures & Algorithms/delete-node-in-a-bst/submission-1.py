# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find node to remove:
        def dfs(node, key):
            if node:
                if node.val == key:
                    # works for both no child and one child
                    if not node.left:
                        return node.right
                    elif not node.right:
                        return node.left
                    # has both children
                    cur = node.right
                    while cur.left:
                        cur = cur.left
                    node.val = cur.val
                    node.right = dfs(node.right, cur.val)
                elif key > node.val:
                    node.right = dfs(node.right, key)
                else:
                    node.left = dfs(node.left, key)
                return node
            # not found
            return None
        
        return dfs(root, key)
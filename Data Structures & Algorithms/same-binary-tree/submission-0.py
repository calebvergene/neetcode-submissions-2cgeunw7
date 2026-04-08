# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def lol(p, q, result):
            if (not p and q) or (not q and p):
                return False
            elif not p and not q:
                return True
            elif p.val != q.val:
                return False
            resultl = lol(p.left, q.left, result)
            resultr = lol(p.right, q.right, result)
            return resultl and resultr
        return lol(p, q, True)



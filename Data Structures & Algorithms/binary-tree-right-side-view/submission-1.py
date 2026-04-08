# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS 
        # return the right most node on the level
        if not root: return []
        right_side = []
        q = collections.deque([root])
        while q:
            depth = len(q)
            for _ in range(depth):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            # now append the last node as that is the one most on the right 
            right_side.append(node.val)
        return right_side
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side = []
        q = deque()
        if root:
            q.append(root)

        while q:
            level_len = len(q)
            for i in range(level_len):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if i == level_len-1: # hit the last node of the level
                    right_side.append(node.val)
        return right_side
                
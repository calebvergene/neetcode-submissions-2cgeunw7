# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS. to begin, i know i need to track height from the top down. 
        if not root: return []
        final = []
        q = collections.deque([root])

        while q:
            level = len(q)
            level_list = []
            for _ in range(level):
                node = q.popleft()
                level_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            final.append(level_list)
        return final
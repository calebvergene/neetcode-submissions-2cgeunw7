# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## for this, I can do dfs and start at the bottom left
        ## i go left, middle, right 
        ## this order will start from smallest to largest
        count, kth_smallest = 0, 0
        def DFS(node):
            nonlocal count
            if count > k:
                return node
            if node == None:
                return 
            
            DFS(node.left)
            count += 1
            if count == k:
                nonlocal kth_smallest
                kth_smallest = node.val
            DFS(node.right)

            return node
        DFS(root)
        return kth_smallest
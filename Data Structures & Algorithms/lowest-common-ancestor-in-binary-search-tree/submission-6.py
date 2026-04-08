# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ## go thgru the tree. when reversing, track bool vals for right and left 
        ## if the numbers were in there, or a list to track if it was in. 
        ## then track a global var with the node that is the first to have the 
        ## descendants on its right/left side 
        # found will be [bool, bool] for if p and q is found
        
        # Move the lowest variable inside the method
        lowest = [None, float('inf')]
        
        def trackHistory(node, found, depth):
            if not node:
                return [False, False], 0
            left, depthl = trackHistory(node.left, [False, False], depth)
            right, depthr = trackHistory(node.right, [False, False], depth)

            if node.val == p.val:
                found[0] = True
            elif node.val == q.val:
                found[1] = True
            
            found = [found[0] or left[0] or right[0], found[1] or left[1] or right[1]]

            depth = max(depthl, depthr)
            if found == [True, True]:
                # Use nonlocal instead of global
                nonlocal lowest
                if depth < lowest[1]:
                    lowest = [node, depth]

            return found, 1+depth
            
        trackHistory(root, [False, False], 0)
        return lowest[0]
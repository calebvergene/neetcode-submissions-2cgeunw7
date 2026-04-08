# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # so my though process, each node needs to be larger than something and less than something
        valid = True
        def isValid(node, less=1001, greater=-1001):
            # base case when reach bottom
            if not node:
                return None
            # check if node is not valid
            if node.val >= less or node.val <= greater:
                nonlocal valid
                valid = False
            
            # child on left needs to be less than parent val, 
            # child on right needs to be greater than parent val, 
            # then pass on less and greater from previous parents to abide by BS rule. 
            left = isValid(node.left, node.val, greater)
            right = isValid(node.right, less, node.val)
        isValid(root)
        return valid



        
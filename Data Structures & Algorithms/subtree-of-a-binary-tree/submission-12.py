# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ## traverse thru whole tree. if the node of the tree u iterate to 
        ## equals the root of the subtree, start comparing them. 

        ## function to start traversing both root and subroot when match
        def checkSubRoot(node, subNode) -> bool:
            if not node and not subNode:
                return True
            elif (not node and subNode) or (node and not subNode):
                return False
            elif node.val != subNode.val:
                return False
            
            left_same = checkSubRoot(node.left, subNode.left)
            right_same = checkSubRoot(node.right, subNode.right)

            return left_same and right_same

        def traverse(node, subRoot) -> bool:
            if not node:
                return False
            if checkSubRoot(node, subRoot):
                return True
            print(node.val, subRoot.val)
            left_same = traverse(node.left, subRoot)
            right_same = traverse(node.right, subRoot)
            return left_same or right_same
        
        return traverse(root, subRoot)






            
            
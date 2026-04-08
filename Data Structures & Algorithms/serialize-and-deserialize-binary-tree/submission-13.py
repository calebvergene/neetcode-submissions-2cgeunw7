# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # ik how to do this. make a list the size of the amount of possible
    # nodes of the level of the tree (depth:3, list = 1+2+4), as if it 
    # were a completely full tree. the empty slots will be None

    # in order traversal: go parent to children. 
    # find children from parent = 2i+1 for left, 2i+2 for right

    # when adding to list, if index of children larger then len of list, keep appending 
    # None to the list. if its smaller, then you can just edit the existing index. 

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodelst = []
        q = deque()
        q.append(root)
        # so we know when the tree has a next level that would just be all None
        next_level = True
        while next_level:
            next_level = False
            for _ in range(len(q)):
                curr = q.popleft()
                # curr is none, AKA it was a filler
                if not curr:
                    nodelst.append(None)
                    q.append(None)
                    q.append(None)
                else:
                    nodelst.append(curr.val)
                    if curr.left or curr.right:
                        next_level = True
                    q.append(curr.left)
                    q.append(curr.right)
        return str(nodelst)
     
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        import ast
        data = ast.literal_eval(data)

        q = deque() 
        root = TreeNode(data[0]) if data[0] else None
        q.append(root)
        i = 0
        while i <= (len(data)-2)//2:
            print(i)
            print(data[2*i + 1], data[2*i + 2])
            print(data)
            curr = q.popleft()
            if not curr:
                q.append(None)
                q.append(None)
            else:
                if data[2*i + 1]:
                    curr.left = TreeNode(data[2*i + 1])
                    q.append(curr.left)
                else:
                    q.append(None)
                if data[2*i + 2]:

                    curr.right = TreeNode(data[2*i + 2])
                    q.append(curr.right)
                else:
                    q.append(None)
            i += 1
        return root 
            



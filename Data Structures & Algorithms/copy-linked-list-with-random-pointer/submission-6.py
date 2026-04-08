"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # use dfs for the random nodes
        nodes = {}

        # basically makes nodes for all of the nodes along random path
        def dfs(node):
            # base case
            if not node:
                return None
            # node already exists, can end chain
            elif node in nodes:
                return nodes[node]
            # node does not exist, need to add it to base case
            # THIS IS WHERE I WAS MESSING UP: 
            # i just had new = node(val, dfs(), dfs()) and then adding it 
            # to the dict after. BUT, THIS WOULD RESULT IN INFINITE RECURSION
            new = Node(node.val)
            nodes[node] = new
            # now I can recursion that I saved my spot
            new.next = dfs(node.next)
            new.random = dfs(node.random)
            return new
        return dfs(head)





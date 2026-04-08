# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i, node in enumerate(lists):
            # i is the tiebreaker if node vals the same
            heapq.heappush(pq, (node.val, i, node))
        root = ListNode()
        curr = root
        tiebreaker = 0
        while pq:
            n = heapq.heappop(pq)[-1] # get the actual node
            curr.next = n
            if n.next:
                heapq.heappush(pq, (n.next.val, tiebreaker, n.next))
            tiebreaker += 1
            curr = curr.next
        return root.next

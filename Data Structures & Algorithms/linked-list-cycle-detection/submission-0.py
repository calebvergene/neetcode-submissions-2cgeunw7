# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        history = []
        current = head
        while current != None:
            if current.val in history:
                return True
            history.append(current.val)
            current = current.next
        return False
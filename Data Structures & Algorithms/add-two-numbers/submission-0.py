# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        place = 1
        # finds total sum from the two linked lists
        while l1 or l2:
            x = 0 if not l1 else l1.val
            y = 0 if not l2 else l2.val
            total += (x + y) * place
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            place = place * 10

        total = str(total)
        head = ListNode(-1)
        curr = head
        for char in total[::-1]:
            curr.next = ListNode(int(char))
            curr = curr.next
        return head.next

            
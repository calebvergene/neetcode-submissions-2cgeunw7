# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find length of list 
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        if length == 1 or length == 2:
            return
            

        # find the split then reverse
        curr = head
        for i in range(math.ceil(length/2)):
            prev = curr
            curr = curr.next
        prev.next = None
        # reverse
        prev = curr
        curr = curr.next 
        prev.next = None
        while curr:
            print(curr.val)
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        end = prev 

        # combine with zip
        while head or end:
            head_next = head.next
            head.next = end
            head = head_next
            if end:
                end_next = end.next
                end.next = head
                end = end_next
        



        
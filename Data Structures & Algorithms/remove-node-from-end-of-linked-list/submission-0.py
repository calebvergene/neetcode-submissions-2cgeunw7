# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## my thought process: have two pointers going thru. 
        ## one starts, and then the other is n nodes behind. when the 
        ## last node hits null, then remove the second pointer. 

        ## edge cases:
        ## if remove head (n = length)
        ## if len = 1

        distance = 0
        start, remove, behind = head, head, head
        while start:
            start = start.next
            if distance >= n:
                remove = remove.next
                ## need a pointer behind remove node to reconnect linked list
                if distance >= n+1:
                    behind = behind.next
            distance += 1
        
        # len = 1
        if distance == 1:
            return
        elif remove == head:
            return head.next
        

        behind.next = remove.next
        remove.next = None
        return head
        ## so from here, behind points to the node to delete


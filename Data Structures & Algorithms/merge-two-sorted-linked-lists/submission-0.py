# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ## Need to iterate through both lists
        current = ListNode()
        head = current
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next
        if list1 == None:
            current.next = list2
        else:
            current.next = list1
        return head.next
        
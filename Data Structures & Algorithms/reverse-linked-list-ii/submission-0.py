# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # reverse linked list starting and ending at positions
        
        # save the left and node before left:
        # the left node will be the end and the other will point to the right

        curr = head
        i = 1
        left_node = None
        before_left = None
        prev = None
        while curr and i <= right:
            if i == left:
                # store left node and the node before left
                left_node = curr
                before_left = prev
                prev = curr
                curr = curr.next
            elif i > left and i < right:
                # start reversing
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            elif i == right:
                if before_left:
                    before_left.next = curr
                else:
                    print(i, curr.val)
                    head = curr
                left_node.next = curr.next
                curr.next = prev
            else:
                prev = curr
                curr = curr.next
            i += 1
        print(head.val)
        return head


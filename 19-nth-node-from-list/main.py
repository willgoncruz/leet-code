# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        size = 0
        while p is not None:
            p = p.next
            size += 1

        p = head
        previous = None
        pos = size - n
        while pos > 0 and p is not None:
            pos -= 1
            previous = p
            p = p.next

        if previous is not None:
            previous.next = p.next
        else:
            return head.next

        return head

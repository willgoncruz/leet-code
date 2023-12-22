# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swap(self, head):
        if head == None or head.next == None:
            return head
        
        continuation = self.swap(head.next.next)
        temp = head.next
        head.next = continuation
        temp.next = head
        
        return temp
    
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        return self.swap(head)

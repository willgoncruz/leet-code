# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        result = None
        if list1.val < list2.val:
            result = list1
            list1 = list1.next
        else:
            result = list2
            list2 = list2.next
            
        start = result
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
                result = result.next
            else:
                result.next = list2
                list2 = list2.next
                result = result.next
                
        if list1 == None:
            result.next = list2
        else:
            result.next = list1
            
        return start

package leet

/**
 * Definition for singly-linked list.
*/

type ListNode struct {
  Val int
  Next *ListNode
}

func getFinalNext(accumulated int) *ListNode {
    if accumulated > 0 {
        return &ListNode{ Val: accumulated, Next: nil }
    }
    
    return nil
}

func getNonNullListNode(l *ListNode) *ListNode {
    if l == nil {
        return &ListNode{ Val: 0, Next: nil }
    }
    
    return l
}

func t(l1 *ListNode, l2 *ListNode, accumulated int) *ListNode {
    if l1 == nil && l2 == nil {
        if accumulated > 0 {
            return &ListNode{ Val: accumulated, Next: nil }
        }
        return nil
    }
    
    l1 = getNonNullListNode(l1)
    l2 = getNonNullListNode(l2)
    
    sum := l1.Val + l2.Val + accumulated
    pass := sum / 10
    r := &ListNode{ Val: sum % 10, Next: nil }
    r.Next = t(l1.Next, l2.Next, pass)
    
    return r
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    first := t(l1, l2, 0)
    return first
}

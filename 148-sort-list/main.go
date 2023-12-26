package leet

type ListNode struct {
  Val int
  Next *ListNode
}


func position(head *ListNode, list *ListNode) *ListNode {
  if list == nil {
    head.Next = nil
    return head
  }
  
  if head.Val <= list.Val {
    head.Next = list
    return head
  }
  
  list.Next = position(head, list.Next)
  return list
}

func recursiveOrder(head *ListNode) *ListNode {
  if head == nil || head.Next == nil {
    return head
  }
  
  n := recursiveOrder(head.Next)
  return position(head, n)
}

func sortList(head *ListNode) *ListNode {
  return recursiveOrder(head)
}

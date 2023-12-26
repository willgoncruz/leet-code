package leet

type ListNode struct {
  Val int
  Next *ListNode
}

func reorderList(head *ListNode)  {
  cp := head
  
  n := 0
  array := []*ListNode{}
  
  for cp != nil {
      array = append(array, cp)
      cp = cp.Next
      n = n + 1
  }
  
  i := 0
  for i < n - i - 1 {
      last := array[n - i - 1]
      saved := head.Next
      head.Next = last
      last.Next = saved
      head = saved
      i = i + 1
  }
  
  head.Next = array[i]
  head.Next.Next = nil
}

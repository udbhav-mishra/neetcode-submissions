# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tail = slow.next
        slow.next = None
        prev = None
        
        while tail:
            nxt = tail.next
            tail.next = prev
            prev = tail
            tail = nxt
        
        dummy = ListNode()
        dummy.next = head
        
        while prev:
            temp1 = head.next
            temp2 = prev.next
            head.next = prev
            prev.next = temp1
            head = temp1
            prev = temp2
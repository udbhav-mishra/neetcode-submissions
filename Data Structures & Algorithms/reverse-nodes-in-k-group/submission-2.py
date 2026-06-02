# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prev, curr, count = dummy, head, 0

        while curr:
            count += 1
            curr = curr.next

        while count >= k:    
            curr = prev.next
            nxt = curr.next

            for _ in range(k - 1):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            
            count -= k
            prev = curr
        return dummy.next
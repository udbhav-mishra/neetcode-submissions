# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = self.getkth(groupPrev, k)
            if not kth: break

            prev, curr = kth.next, groupPrev.next
            groupNext = kth.next
            
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next

    def getkth(self, curr, k):

        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr
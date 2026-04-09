# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total  = 0
        a = head
        while a:
            a = a.next
            total += 1
        if total == n:
            return head.next
        b = head
        for _ in range(total - n - 1):
            b = b.next
        if b.next:
            b.next = b.next.next
        return head
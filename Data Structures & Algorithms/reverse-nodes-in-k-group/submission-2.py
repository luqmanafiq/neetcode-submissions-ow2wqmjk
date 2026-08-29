# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        new_head = None
        ktail = None

        while cur:
            count = 0
            cur = head
            while count < k and cur:
                cur = cur.next
                count += 1
            if count == k:
                rev_head = self.reverse(head, k)
                if not new_head:
                    new_head = rev_head
                if ktail:
                    ktail.next = rev_head
                ktail = head
                head = cur
        if ktail:
            ktail.next = head
        return new_head if new_head else head

    def reverse(self, head, k):
        new_head = None
        prev = head
        while k:
            next_node = prev.next
            prev.next = new_head
            new_head = prev
            prev = next_node
            k -= 1
        return new_head
        
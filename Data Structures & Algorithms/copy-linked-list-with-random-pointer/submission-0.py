"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        map = {}

        cur = head
        while cur:
            map[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            new_node = map[cur]
            new_node.next = map.get(cur.next)
            new_node.random = map.get(cur.random)
            cur = cur.next
        return map[head]
            

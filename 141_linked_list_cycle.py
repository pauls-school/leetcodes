# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        if node:
            while node.next:
                if node.next.val == 100001:
                    return True
                else:
                    node.val = 100001
                    node = node.next
        return False

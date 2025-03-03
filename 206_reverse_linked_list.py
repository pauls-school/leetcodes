# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        normal_node = head
        prev = None
        while normal_node:
            reverse_node = ListNode(normal_node.val)
            if prev:
                reverse_node.next = prev
            else:
                reverse_node.next = None
            normal_node = normal_node.next
            prev = reverse_node
        return reverse_node

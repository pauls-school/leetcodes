# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        sum_ll = ListNode()
        list1 = []
        list2 = []
        while node1 or node2:
            if node1 and node2:
                list1.insert(0, node1.val)
                list2.insert(0, node2.val)
                node1 = node1.next
                node2 = node2.next
            elif node1:
                return ListNode(69)
            elif node2:
                return ListNode(69)
            print(list1, list2)
            # node1 = node1.next
            # node2 = node2.next

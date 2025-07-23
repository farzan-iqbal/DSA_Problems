# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        current = head

        while current:
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            next_node = current.next
            current.next = prev.next
            prev.next = current
            current = next_node

        return dummy.next

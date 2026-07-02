# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head

        while current:
            if current.val == 1001:
                return True
            else:
                current.val = 1001
            current = current.next
        return False
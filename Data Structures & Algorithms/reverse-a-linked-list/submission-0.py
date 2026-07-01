# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        previous = head
        current = previous.next
        previous.next = None


        while current.next != None:
            print(previous.val, current.val, current.next.val)
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        current.next = previous
        head = current
        return head
        
        

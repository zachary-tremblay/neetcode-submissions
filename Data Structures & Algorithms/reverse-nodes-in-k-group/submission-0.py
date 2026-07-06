# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ptr1 = ListNode()
        ptr1.next = head
        ptr2 = ptr1

        while True:
            ptr2 = ptr1
            for i in range(k):
                ptr2 = ptr2.next
                if not ptr2:
                    return dummy.next
            
            groupHead = ptr1.next
            afterGroup = ptr2.next
            
            newHead = self.reverse(groupHead, afterGroup, k)
            ptr1.next = newHead
            ptr1 = groupHead

        return dummy.next


    
    def reverse(self, head:Optional[ListNode], nxt:Optional[ListNode], k:int) -> Optional[ListNode]:
        prev, curr = nxt, head

        while curr != nxt:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
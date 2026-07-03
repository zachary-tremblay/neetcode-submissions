# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #size 1
        if not head.next:
            head = None
            return head
        #last
        elif n == 1:
            curr = head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            return head

        #middle/end
        else:
            curr = head
            length = 0
            while curr:
                curr = curr.next
                length += 1
            if length == n:
                head = head.next
                return head

            fromStart = length - n
            curr = head
            for i in range(fromStart):
                previous = curr
                curr = curr.next
                i += 1
                print(previous.val, curr.val)
            previous.next = curr.next
            return head


        
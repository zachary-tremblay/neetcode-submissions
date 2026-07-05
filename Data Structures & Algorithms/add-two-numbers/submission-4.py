# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = l1, l2
        head = curr1
        carry = 0
        while curr1 or curr2 or carry:

            curr1Val = curr1.val if curr1 else 0
            curr2Val = curr2.val if curr2 else 0

            valSum = curr1Val + curr2Val + carry
            if curr1:
                curr1.val = valSum % 10
            else:
                curr1 = ListNode(valSum % 10)
                prev.next = curr1

            carry = valSum // 10

            prev = curr1
            
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        
        return head

                






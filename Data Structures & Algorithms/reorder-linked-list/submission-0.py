# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #push them all in a stack
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next

        current = head
        #start from head, get previous, point previous to top of the stack, repeat for half stack size
        for i in range(len(stack)//2):
            previous = current
            current = current.next
            previous.next = stack.pop()
            previous.next.next = current
        current.next = None

        return
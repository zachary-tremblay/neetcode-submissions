# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            temp = list1.next
            head = list1
            list1 = temp
        else:
            temp = list2.next
            head = list2
            list2 = temp

        current = head
        while list1 and list2:
            if list1 and list1.val <= list2.val:
                temp = list1.next
                current.next = list1
                list1 = temp
            else:
                temp = list2.next
                current.next = list2
                list2 = temp
            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2

        return head
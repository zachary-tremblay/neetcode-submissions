# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        idx = 0
        dummy = current = ListNode()

        while lists:
            minValue = float('infinity')
            for i, head in enumerate(lists):
                
                if head and head.val < minValue:
                    minValue = head.val
                    idx = i
            
            if lists[idx] == None:
                break
            current.next = lists[idx]
            lists[idx] = lists[idx].next if lists[idx].next else None
            current = current.next

        return dummy.next
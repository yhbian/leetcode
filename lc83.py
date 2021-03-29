# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        ret = head
        while head and head.next:
            x = head.val
            while head.next and head.next.val == x:
                head.next = head.next.next
            head = head.next
        return ret
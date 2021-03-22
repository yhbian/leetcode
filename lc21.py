class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None

        # init the head
        if l1 and not l2:
            head = ListNode(l1.val)
            l1 = l1.next
        elif l2 and not l1:
            head = ListNode(l2.val)
            l2 = l2.next
        elif l1.val > l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next
        node = head
            
        while l1 and l2:
            if l1.val < l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next
            node = node.next
        
        if l1:
            while l1:
                node.next = ListNode(l1.val)
                l1 = l1.next
                node = node.next

        if l2:
            while l2:
                node.next = ListNode(l2.val)
                l2 = l2.next
                node = node.next

        return head



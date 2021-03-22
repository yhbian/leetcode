class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

class Solution:
    def removeNthFromEnd(self, head, n):
        ret_list = list()
        node = head
        while node:
            ret_list.append(node.val)
            node = node.next
        if len(ret_list) < n:
            return head
        ret_list.pop(-n)

        if not ret_list:
            return None
        ret = ListNode()
        node = ret
        idx = 0
        while idx < len(ret_list):
            node.val = ret_list[idx]
            if idx == len(ret_list)-1:
                idx += 1
                return ret
            node.next = ListNode()
            node = node.next
            idx += 1


        
        

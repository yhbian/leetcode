import LinkList


class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        full = 0
        if l1.val + l2.val < 10:
            sum_node = ListNode(l1.val + l2.val)
        else:
            sum_node = ListNode(l1.val + l2.val - 10)
            full = 1
        sum_ = sum_node
        l1, l2 = l1.next, l2.next
        while l1 or l2:
            a, b = 0, 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            temp = a + b
            if temp + full < 10:
                sum_.next = ListNode(temp + full)
                full = 0
            else:
                sum_.next = ListNode(temp + full - 10)
                full = 1
            sum_ = sum_.next

        if not full:
            return sum_node
        else:
            sum_.next = ListNode(1)
            return sum_node


if __name__ == '__main__':
    l1, l2 = LinkList._construct_link([9]), LinkList._construct_link([9])
    out = Solution().addTwoNumbers(l1, l2)
    LinkList._visualize_link(out)


